
# Network TTL Analyzer (PowerShell)

A lightweight PowerShell utility to analyze ICMP TTL values across a list of IP addresses and identify devices with low TTL responses.

This script is useful for network discovery, troubleshooting, and identifying non-Windows or routed devices within a network.

---

## 🔍 What This Script Does

- Reads a list of IP addresses from a text file
- Sends a single ICMP ping to each IP
- Extracts the TTL (Time To Live) value from the response
- Saves IPs with **TTL lower than a defined threshold (default: 64)** into an output file

---

## 🎯 Why TTL < 64 Matters

A TTL value lower than 64 often indicates:
- Linux-based systems
- Routers, firewalls, or network appliances
- Devices behind NAT or tunnels
- Increased hop count (routing path analysis)

This makes the script useful for:
- Network reconnaissance
- Device classification
- Pre-filtering targets for automation
- Troubleshooting routing or tunneling issues

---

## 📂 File Structure

ttl-analyzer/ ├── check_low_ttl.ps1 ├── ip_list.txt └── low_ttl_ips.txt

---

## ▶️ How to Use

1. Edit `ip_list.txt` and add one IP address per line.
2. Open PowerShell **as Administrator**.
3. Run the script:

```powershell
.\check_low_ttl.ps1

4. Results will be saved to:



low_ttl_ips.txt


---

🛠 Requirements

Windows

PowerShell 5.x or newer

ICMP (Ping) allowed on the network



---

📌 Output Example

192.168.1.1 - TTL: 62
10.10.10.254 - TTL: 58


---

🚀 Future Improvements (Optional)

Make TTL threshold configurable

Parallel ping for faster execution

CSV output support

Automatic OS fingerprinting



---

👨‍💻 Author

Network Automation Toolkit
PowerShell & Network Engineering Utilities
