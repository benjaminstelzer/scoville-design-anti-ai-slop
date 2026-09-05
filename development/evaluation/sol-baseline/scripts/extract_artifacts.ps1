param(
    [Parameter(Mandatory = $true)]
    [string]$RunRoot,

    [Parameter(Mandatory = $true)]
    [string]$OutputRoot
)

$ErrorActionPreference = 'Stop'

$resolvedRunRoot = (Resolve-Path -LiteralPath $RunRoot).Path
$predictionRoot = Join-Path $resolvedRunRoot 'predictions'

if (-not (Test-Path -LiteralPath $predictionRoot -PathType Container)) {
    throw "Prediction directory not found: $predictionRoot"
}

[System.IO.Directory]::CreateDirectory($OutputRoot) | Out-Null

$supportedExtensions = @{
    'svg'  = '.svg'
    'html' = '.html'
}

$records = foreach ($resultFile in Get-ChildItem -LiteralPath $predictionRoot -Filter 'result.json' -Recurse -File) {
    $result = Get-Content -Raw -LiteralPath $resultFile.FullName | ConvertFrom-Json -Depth 100
    $prediction = $result.predicted_answer
    $format = [string]$prediction.artifact_format

    if (-not $supportedExtensions.ContainsKey($format)) {
        continue
    }

    $caseDirectory = Join-Path $OutputRoot ([string]$result.id)
    [System.IO.Directory]::CreateDirectory($caseDirectory) | Out-Null

    $artifactPath = Join-Path $caseDirectory ("artifact" + $supportedExtensions[$format])
    [System.IO.File]::WriteAllText(
        $artifactPath,
        [string]$prediction.artifact,
        [System.Text.UTF8Encoding]::new($false)
    )

    $metadata = [ordered]@{
        id = [string]$result.id
        task_type = [string]$result.task_type
        artifact_format = $format
        design_read = [string]$prediction.design_read
        self_critique = @($prediction.self_critique)
        rendered_status = [string]$prediction.rendered_status
        hard = $result.hard
        soft = $result.soft
        skill_tokens = $result.skill_tokens
        total_tokens = $result.tokens.total
        source_result = $resultFile.FullName
        artifact = $artifactPath
    }

    $metadataPath = Join-Path $caseDirectory 'metadata.json'
    [System.IO.File]::WriteAllText(
        $metadataPath,
        ($metadata | ConvertTo-Json -Depth 20),
        [System.Text.UTF8Encoding]::new($false)
    )

    $metadata
}

$records | ConvertTo-Json -Depth 20
