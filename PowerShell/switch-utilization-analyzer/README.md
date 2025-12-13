# Cisco Switch Utilization Analyzer (PowerShell)

A PowerShell-based text analysis tool designed to evaluate Cisco switch utilization by parsing raw CLI outputs and identifying heavily-used access switches.

This script is useful for capacity planning, auditing, and infrastructure optimization.

---

## 🔍 What This Script Does

- Parses a raw text file containing multiple Cisco switch outputs
- Splits device data into logical blocks
- Extracts:
  - Device name
  - Cisco model
  - Number of connected access ports
- Excludes specific switch models using a configurable exclusion list
- Filters devices with high port utilization (default: ≥ 20 connected ports)
- Outputs results to console and CSV

---

## 📂 File Structure

switch-utilization-analyzer/ ├── analyze_switch_ports.ps1 ├── yas.txt ├── excluded_models.txt └── FilteredDevices.csv

---

## ▶️ How to Use

1. Place all switch outputs inside `yas.txt`
2. Add unwanted models (e.g. 48-port switches) to `excluded_models.txt`
3. Update file paths inside the script if needed
4. Run the script in PowerShell:

```powershell
.\analyze_switch_ports.ps1


---

📊 Output

Console table sorted by connected ports

CSV report sorted by utilization


CSV Columns

DeviceName

Model

ConnectedPorts



---

🎯 Use Cases

Identify overloaded access switches

Capacity planning and upgrade decisions

Network inventory analysis

Pre-migration audits

Infrastructure optimization



---

🛠 Requirements

Windows

PowerShell 5.x+

Raw Cisco CLI output (show version, show interface status)



---

🚀 Possible Enhancements

Configurable utilization threshold

Support for TenGig / Ethernet interfaces

JSON output

Auto-detection of switch role (Access / Distribution)



---

👨‍💻 Author

Network Automation Toolkit
PowerShell Network Analysis Utilities
