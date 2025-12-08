from routeros_api import RouterOsApiPool
from datetime import datetime

MIKROTIK_IP = "192.168.1.1"
USERNAME = "admin"
PASSWORD = "password"

api_pool = RouterOsApiPool(
    MIKROTIK_IP,
    username=USERNAME,
    password=PASSWORD,
    plaintext_login=True
)

api = api_pool.get_api()
interfaces = api.get_resource('/interface/print')

now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"mikrotik_interfaces_{now}.txt"

with open(filename, "w") as file:
    for iface in interfaces:
        file.write(str(iface) + "\n")

print("[+] MikroTik interfaces backup saved.")

api_pool.disconnect()
