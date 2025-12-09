import requests
import csv

PRTG_URL = "https://your-prtg-server/api/table.csv"
USERNAME = "username"
PASSHASH = "passhash"
OBJECTID = "36119"

params = {
    "content": "sensors",
    "columns": "objid,name,lastvalue,status",
    "username": USERNAME,
    "passhash": PASSHASH
}

try:
    response = requests.get(f"{PRTG_URL}?id={OBJECTID}", params=params, verify=False)
    with open("prtg_report.csv", "w", newline="") as f:
        f.write(response.text)
    print("CSV exported successfully")

except Exception as e:
    print(f"Error: {e}")