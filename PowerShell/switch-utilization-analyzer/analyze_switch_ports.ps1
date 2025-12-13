


# Paths to your files
$yasFile = "C:\path\to\yas.txt"
$excludedFile = "C:\path\to\48p.txt"
$outputCsv = "C:\path\to\FilteredDevices.csv"

# Load exclusion list
$excludedModels = Get-Content $excludedFile | Where-Object { $_.Trim() -ne "" }

# Read all lines from yas.txt
$content = Get-Content $yasFile -Raw

# Split into device blocks (separated by long underscores)
$deviceBlocks = $content -split "_{75,}\r?\n\r?\n"

$results = @()

foreach ($block in $deviceBlocks) {
    if ($block.Trim() -eq "") { continue }

    # Extract device name (first word before the first '(' or space)
    if ($block -match "^(?<DeviceName>[A-Za-z0-9_\-\.]+)") {
        $deviceName = $matches['DeviceName']
    } else {
        continue
    }

    # Extract model from the block (line starting with 'cisco' or 'Cisco')
    $model = ""
    if ($block -match "(?im)^cisco\s+(.+)$") {
        $model = $matches[1].Trim()
    }

    # Skip if model contains any excluded keyword
    $isExcluded = $false
    foreach ($excl in $excludedModels) {
        if ($model -like "*$excl*") {
            $isExcluded = $true
            break
        }
    }
    if ($isExcluded) { continue }

    # Count connected ports (lines starting with Fa or Gi and 'connected')
    $connectedCount = ([regex]::Matches($block, "^(Fa|Gi)\S+\s+connected", 'Multiline')).Count

    if ($connectedCount -ge 20) {
        $results += [PSCustomObject]@{
            DeviceName     = $deviceName
            Model          = $model
            ConnectedPorts = $connectedCount
        }
    }
}

# Output sorted list to console
$results | Sort-Object ConnectedPorts -Descending | Format-Table -AutoSize

# Export to CSV
$results | Sort-Object ConnectedPorts -Descending | Export-Csv -Path $outputCsv -NoTypeInformation -Encoding UTF8

# Show total count
Write-Host "`nTotal devices found:" $results.Count
Write-Host "Results saved to: $outputCsv"


