from Mikrotik_Connector import Mikrotik

router_ip = "192.168.88.1"
username = "admin"
password = "password"

# File containing IPs
file_path = "aggregated_ips.txt"

try:
    router = Mikrotik(router_ip, username, password)

    with open(file_path) as f:
        ip_list = [line.strip() for line in f if line.strip()]

    for ip in ip_list:
        try:
            router.add_firewall_addresslist(list_name="BLOCKED", address=ip)
            print(f"Added {ip} to BLOCKED list")
        except Exception as e:
            print(f"Error adding {ip}: {e}")

except Exception as e:
    print(f"Error: {e}")
finally:
    router.disconnect()