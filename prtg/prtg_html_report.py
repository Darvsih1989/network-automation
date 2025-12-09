import requests
from datetime import datetime

# PRTG server info
PRTG_URL = "https://your-prtg-server/api/table.json"
USERNAME = "username"
PASSHASH = "passhash"  # or API token
OBJECTID = "36119"  # Sensor or Device ID

params = {
    "content": "sensors",
    "columns": "objid,name,lastvalue,status",
    "username": USERNAME,
    "passhash": PASSHASH
}

try:
    response = requests.get(f"{PRTG_URL}?id={OBJECTID}", params=params, verify=False)
    data = response.json()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"prtg_report_{timestamp}.html"

    with open(filename, "w") as f:
        f.write("<html><body><h2>PRTG Report</h2><table border='1'>")
        f.write("<tr><th>ID</th><th>Name</th><th>Last Value</th><th>Status</th></tr>")

        for sensor in data.get("sensors", []):
            f.write(f"<tr><td>{sensor['objid']}</td><td>{sensor['name']}</td>"
                    f"<td>{sensor['lastvalue']}</td><td>{sensor['status']}</td></tr>")

        f.write("</table></body></html>")

    print(f"HTML report saved as {filename}")

except Exception as e:
    print(f"Error: {e}")