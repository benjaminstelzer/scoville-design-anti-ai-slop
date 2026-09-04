param(
    [Parameter(Mandatory = $true)]
    [string]$ArtifactRoot
)

$ErrorActionPreference = 'Stop'
$resolvedRoot = (Resolve-Path -LiteralPath $ArtifactRoot).Path

$records = foreach ($artifact in Get-ChildItem -LiteralPath $resolvedRoot -Recurse -File |
    Where-Object { $_.Name -in @('artifact.svg', 'artifact.html') }) {
    $format = $artifact.Extension.TrimStart('.')
    $parseOk = $true
    $parseError = ''
    $rootElement = ''

    if ($format -eq 'svg') {
        try {
            $document = [System.Xml.XmlDocument]::new()
            $document.PreserveWhitespace = $true
            $document.Load($artifact.FullName)
            $rootElement = $document.DocumentElement.LocalName
            if ($rootElement -ne 'svg') {
                throw "Root element is '$rootElement', not 'svg'."
            }
        }
        catch {
            $parseOk = $false
            $parseError = $_.Exception.Message
        }
    }
    else {
        $source = Get-Content -Raw -LiteralPath $artifact.FullName
        $rootElement = if ($source -match '(?is)<html\b') { 'html' } else { '' }
        if ($rootElement -ne 'html') {
            $parseOk = $false
            $parseError = 'No html root element found.'
        }
    }

    $renderPath = Join-Path $artifact.DirectoryName 'render-full.png'
    [ordered]@{
        artifact = $artifact.FullName
        format = $format
        parse_ok = $parseOk
        parse_error = $parseError
        root_element = $rootElement
        render_exists = Test-Path -LiteralPath $renderPath -PathType Leaf
        render = $renderPath
    }
}

$records | ConvertTo-Json -Depth 10
