from Mikrotik_Connector import Mikrotik

router_ip = "192.168.88.1"
username = "admin"
password = "password"

try:
    router = Mikrotik(router_ip, username, password)
    info = router.system_identity()
    print(f"Connected successfully to: {info}")

except Exception as e:
    print(f"Connection failed: {e}")
finally:
    router.disconnect()