🚀 Network Automation Toolkit

A Complete Collection of Real-World Network Automation Scripts

Automating Cisco, MikroTik, PRTG, Selenium, Docker Labs, and Infrastructure Tasks


---

📌 Introduction

This repository is a complete toolkit of real-world, production-grade Network Automation scripts, created and tested across multiple devices and environments including:

Cisco IOS / IOS-XE

Cisco Nexus

MikroTik RouterOS

PRTG Monitoring System

Selenium Web Automation

Excel & CSV Automation

Docker-based virtual network labs

SSH automation with Netmiko / Paramiko

Playwright for Web UI automation


All scripts are modular, tested, and ready for real-world enterprise use.


---

📦 Features

✅ Cisco Automation

Backup configurations (IOS, IOS-XE, Nexus)

Logout active Cisco users

ASR 1000 Power Redundancy Monitoring

Multi-device parallel SSH execution

Running CLI commands from file lists


✅ MikroTik Automation

Automated login using Mikrotik_Connector

Backup generation + file download

Firewall address-list automation

Parsing invalid IP formats (/32, ranges, etc.)


✅ PRTG Monitoring Automation

Fetch sensor data using PRTG REST API

CSV export for Receive/Transmit speeds

Full HTML Report Generator

Auto screenshot collector (PRTG graphs)

Daily monitoring automation system


✅ Web Automation (Selenium + Playwright)

Automated login to dashboard systems

Full-page screenshot capture

File download automation without renaming

Handling pop-ups, checkboxes, and collapse sections

Running automation inside WSL (Ubuntu 22.04)


✅ Excel / CSV Automation

Convert .xls → .xlsx using openpyxl

Generate formal Excel tables

Insert Excel tables into PowerPoint slides

Dynamic file attachment automation in email scripts


✅ Docker Infrastructure Labs

Full Linux container with SSH, SNMP, Python

Simulated production-like monitoring lab

Testing SNMP polling and Python automation inside Docker



---

🛠 Requirements

Python 3.10+

Install required dependencies:

pip install -r requirements.txt

Included Libraries:

netmiko
paramiko
requests
openpyxl
python-pptx
selenium
playwright
beautifulsoup4
pandas
matplotlib
mikrotik-connector

Install Playwright Browsers:

playwright install

Install Selenium WebDriver (Firefox recommended):

sudo apt install firefox-geckodriver


---

📂 Project Structure

network-automation/
│
├── cisco/
│   ├── cisco_backup_nexus.py
│   ├── cisco_enable_logout.py
│   ├── asr_power_redundancy.py
│   └── run_commands_from_file.py
│
├── mikrotik/
│   ├── mikrotik_backup.py
│   ├── mikrotik_login.py
│   └── mikrotik_addresslist.py
│
├── prtg/
│   ├── prtg_api_fetch.py
│   ├── prtg_html_report.py
│   ├── prtg_graph_screenshot.py
│   └── prtg_daily_monitor.py
│
├── web_automation/
│   ├── selenium_fullpage_screenshot.py
│   ├── selenium_login.py
│   ├── playwright_interactions.py
│   └── file_download_automation.py
│
├── excel_tools/
│   ├── xls_to_xlsx.py
│   ├── insert_table_to_ppt.py
│   └── csv_ip_validator.py
│
└── docker_lab/
    ├── Dockerfile
    ├── docker-compose.yml
    └── README.md


---

🚀 Usage Examples

🔹 Cisco Backup (Nexus, IOS, IOS-XE)

python cisco/cisco_backup_nexus.py

Backs up all devices listed in:

ssh_con/CiscoBackupIP.txt


---

🔹 MikroTik Address List Automation

python mikrotik/mikrotik_addresslist.py

Automatically adds thousands of IPs from a text file.


---

🔹 PRTG HTML Report Generation

python prtg/prtg_html_report.py

Output example:

reports/prtg_report_2025_01_10.html


---

🔹 Selenium Full Page Screenshot

python web_automation/selenium_fullpage_screenshot.py


---

🔹 Convert .xls to .xlsx

python excel_tools/xls_to_xlsx.py


---

🧪 Docker Lab Setup

Build image:

docker build -t network-lab .

Run environment:

docker-compose up -d

Includes:

Ubuntu container

SSH server

SNMP server

Python scripts

Allows testing polling, automation, and monitoring in isolation



---

📧 Email Automation with Attachments

Supports dynamic:

PBX files

PNG graphs

Multi-file attachments



---

🔍 Future Enhancements

Ansible playbooks

NetBox automation

CI/CD pipeline for testing scripts

FastAPI dashboard for automation jobs


