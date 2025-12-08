import requests
import csv
from datetime import datetime

# ===== PRTG SETTINGS =====
PRTG_URL = "http://YOUR_PRTG_IP/api/table.json"
USERNAME = "prtguser"
PASSHASH = "YOUR_PASSHASH"

# Get sensor data
params = {
    "content": "sensors",
    "output": "json",
    "columns": "objid,device,sensor,status,message,lastvalue",
    "username": USERNAME,
    "passhash": PASSHASH
}

print("[+] Connecting to PRTG API...")

response = requests.get(PRTG_URL, params=params, timeout=15)
data = response.json()

now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"prtg_report_{now}.csv"

with open(filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ObjectID", "Device", "Sensor", "Status", "Message", "Last Value"])

    for sensor in data["sensors"]:
        writer.writerow([
            sensor.get("objid"),
            sensor.get("device"),
            sensor.get("sensor"),
            sensor.get("status"),
            sensor.get("message"),
            sensor.get("lastvalue")
        ])

print(f"[+] PRTG Report saved as {filename}")
