import requests

PRTG_GRAPH_URL = "https://your-prtg-server/chart.png"
USERNAME = "username"
PASSHASH = "passhash"
SENSORID = "36119"

params = {
    "username": USERNAME,
    "passhash": PASSHASH,
    "id": SENSORID,
    "graph": "lastvalue",
    "avg": 3600,
}

try:
    r = requests.get(PRTG_GRAPH_URL, params=params, verify=False)
    with open("prtg_sensor_graph.png", "wb") as f:
        f.write(r.content)
    print("Graph screenshot saved!")

except Exception as e:
    print(f"Error: {e}")