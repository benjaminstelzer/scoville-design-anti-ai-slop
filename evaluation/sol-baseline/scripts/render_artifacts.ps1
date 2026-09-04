param(
    [Parameter(Mandatory = $true)]
    [string]$ArtifactRoot,

    [Parameter(Mandatory = $true)]
    [string]$RepositoryRoot,

    [string]$BaseUrl = 'http://127.0.0.1:8765',

    [switch]$Force
)

$ErrorActionPreference = 'Stop'

$resolvedArtifactRoot = (Resolve-Path -LiteralPath $ArtifactRoot).Path
$resolvedRepositoryRoot = (Resolve-Path -LiteralPath $RepositoryRoot).Path
$normalizedRepositoryRoot = $resolvedRepositoryRoot.TrimEnd('\') + '\'

if (-not $resolvedArtifactRoot.StartsWith($normalizedRepositoryRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "ArtifactRoot must be inside RepositoryRoot."
}

$artifacts = Get-ChildItem -LiteralPath $resolvedArtifactRoot -Recurse -File |
    Where-Object { $_.Name -in @('artifact.svg', 'artifact.html') }

function Convert-ToCssPixels {
    param([Parameter(Mandatory = $true)][string]$Value)

    if ($Value -notmatch '^\s*([0-9]+(?:\.[0-9]+)?)\s*(px|mm|cm|in|pt)?\s*$') {
        return $null
    }

    $number = [double]$Matches[1]
    switch ($Matches[2]) {
        'mm' { return [int][Math]::Ceiling($number * 96 / 25.4) }
        'cm' { return [int][Math]::Ceiling($number * 96 / 2.54) }
        'in' { return [int][Math]::Ceiling($number * 96) }
        'pt' { return [int][Math]::Ceiling($number * 96 / 72) }
        default { return [int][Math]::Ceiling($number) }
    }
}

function Get-SvgViewport {
    param([Parameter(Mandatory = $true)][string]$Path)

    $source = Get-Content -Raw -LiteralPath $Path
    $width = $null
    $height = $null

    if ($source -match '<svg\b[^>]*\bwidth=["'']([^"'']+)["'']') {
        $width = Convert-ToCssPixels $Matches[1]
    }
    if ($source -match '<svg\b[^>]*\bheight=["'']([^"'']+)["'']') {
        $height = Convert-ToCssPixels $Matches[1]
    }
    if (($null -eq $width -or $null -eq $height) -and $source -match '<svg\b[^>]*\bviewBox=["'']\s*[-0-9.]+\s+[-0-9.]+\s+([0-9.]+)\s+([0-9.]+)\s*["'']') {
        if ($null -eq $width) { $width = [int][Math]::Ceiling([double]$Matches[1]) }
        if ($null -eq $height) { $height = [int][Math]::Ceiling([double]$Matches[2]) }
    }

    if ($null -eq $width -or $null -eq $height) {
        throw "SVG has no usable width/height or viewBox: $Path"
    }

    return [ordered]@{ width = $width; height = $height }
}

$records = foreach ($artifact in $artifacts) {
    $relativePath = $artifact.FullName.Substring($normalizedRepositoryRoot.Length).Replace('\', '/')
    $encodedSegments = $relativePath.Split('/') | ForEach-Object { [uri]::EscapeDataString($_) }
    $url = $BaseUrl.TrimEnd('/') + '/' + ($encodedSegments -join '/')
    $renderPath = Join-Path $artifact.DirectoryName 'render-full.png'
    $captureMode = 'full-artifact'

    if ((Test-Path -LiteralPath $renderPath -PathType Leaf) -and -not $Force) {
        [ordered]@{
            artifact = $artifact.FullName
            render = $renderPath
            url = $url
            capture_mode = 'existing'
        }
        continue
    }

    if ($artifact.Extension -eq '.svg') {
        $viewport = Get-SvgViewport $artifact.FullName
        $viewportArgument = "$($viewport.width),$($viewport.height)"
        & npx --yes playwright screenshot --viewport-size=$viewportArgument $url $renderPath
    }
    else {
        & npx --yes playwright screenshot --viewport-size='1440,1100' --full-page $url $renderPath
        if ($LASTEXITCODE -ne 0) {
            $captureMode = 'desktop-viewport-fallback'
            & npx --yes playwright screenshot --viewport-size='1440,1100' $url $renderPath
        }
    }

    if ($LASTEXITCODE -ne 0) {
        throw "Playwright render failed for $($artifact.FullName)."
    }

    [ordered]@{
        artifact = $artifact.FullName
        render = $renderPath
        url = $url
        capture_mode = $captureMode
    }
}

$records | ConvertTo-Json -Depth 10
