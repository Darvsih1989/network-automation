# Network Automation Projects

This repository contains a collection of network automation scripts written in Python.
All projects are categorized as follows:

1. [Cisco Automation](#cisco-automation)
2. [MikroTik Automation](#mikrotik-automation)
3. [PRTG Monitoring Automation](#prtg-monitoring-automation)
4. [Web Automation (Selenium & Playwright)](#web-automation)
5. [File & Excel Automation](#file-excel-automation)
6. [Email Automation](#email-automation)

---

## 📦 Installation

```bash
pip install netmiko openpyxl requests mikrotik-connector selenium playwright
playwright install
```

> Note: Selenium requires Firefox browser and geckodriver installed.

---

## Cisco Automation

**Folder path:** `cisco/`

| File                     | Description                       |
| ------------------------ | --------------------------------- |
| `cisco_backup_single.py` | Backup a single Cisco device      |
| `CiscoBackup_v1.py`      | Multi-device backup (version 1)   |
| `CiscoBackup_v2.py`      | Multi-device backup (version 2)   |
| `CiscoBackup_v3.py`      | Multi-device backup (version 3)   |
| `nexus_backup.py`        | Backup Nexus switches             |
| `cisco_logout_users.py`  | Logout active users               |
| `asr_power_monitor.py`   | Monitor ASR 1000 power redundancy |

**Example execution:**

```bash
python cisco/cisco_backup_single.py
```

---

## MikroTik Automation

**Folder path:** `mikrotik/`

| File                      | Description                 |
| ------------------------- | --------------------------- |
| `mikrotik_backup.py`      | Full MikroTik backup        |
| `mikrotik_login.py`       | Test connection to MikroTik |
| `mikrotik_addresslist.py` | Add IPs to Address List     |

---

## PRTG Monitoring Automation

**Folder path:** `prtg/`

| File                       | Description                      |
| -------------------------- | -------------------------------- |
| `prtg_html_report.py`      | Generate HTML report from PRTG   |
| `prtg_export_csv.py`       | Export CSV report from PRTG      |
| `prtg_graph_screenshot.py` | Take graph screenshots from PRTG |

---

## Web Automation (Selenium & Playwright)

**Folder path:** `web_automation/`

| File                              | Description                             |
| --------------------------------- | --------------------------------------- |
| `selenium_fullpage_screenshot.py` | Full-page screenshot using Selenium     |
| `selenium_login.py`               | Website login automation using Selenium |
| `playwright_automation.py`        | Screenshot using Playwright             |

---

## File & Excel Automation

**Folder path:** `file_automation/`

| File                      | Description                            |
| ------------------------- | -------------------------------------- |
| `excel_read_write.py`     | Read/Write Excel files using openpyxl  |
| `text_file_automation.py` | Read/Write text files                  |
| `aggregate_ips.py`        | Aggregate IPs from multiple text files |

---

## Email Automation

**Folder path:** `email_automation/`

| File                             | Description                  |
| -------------------------------- | ---------------------------- |
| `send_email_smtp.py`             | Send simple emails via SMTP  |
| `send_email_with_attachments.py` | Send emails with attachments |

---

## 👁 Folder Structure

```
network-automation/
├── cisco/
├── mikrotik/
├── prtg/
├── web_automation/
├── file_automation/
└── email_automation/
```

---

## 🔧 Important Notes

* Update **IP addresses, usernames, and passwords** in each script before execution.
* Clone the repository locally to execute scripts with correct folder paths.
* For Web Automation, ensure the required browser and driver are installed.
* For PRTG and MikroTik, API and SSH access are required.

---

## 💡 Recommendation

This repository can serve as a **complete reference for network automation projects**.
Each script can be run individually or extended for further automation tasks.
