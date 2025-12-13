#Path to the file containing IP addresses (one per line)

$ipListPath = "C:\Users\Administrator\Desktop\xlsx_Project\ip_list.txt"

Output file path for IPs with TTL < 64

$outputFile = "C:\Users\Administrator\Desktop\xlsx_Project\low_ttl_ips.txt"

Clear or create the output file

Clear-Content -Path $outputFile -ErrorAction SilentlyContinue
New-Item -Path $outputFile -ItemType File -Force | Out-Null

Read each IP and ping it

Get-Content $ipListPath | ForEach-Object {
$ip = $_.Trim()
if ($ip -ne "") {
# Send one ping request
$pingResult = ping -n 1 $ip

# Check if there's a reply and extract TTL  
    foreach ($line in $pingResult) {  
        if ($line -match "Reply from .*:.*TTL=(\d+)") {  
            $ttl = [int]$matches[1]  
            if ($ttl -lt 64) {  
                "$ip - TTL: $ttl" | Out-File -Append -FilePath $outputFile  
            }  
            break  
        }  
    }  
}

}

Write-Host "Done. Saved IPs with TTL < 64 to $outputFile"
