from netmiko import ConnectHandler
from datetime import datetime

device = {
    'device_type': 'cisco_nxos',
    'host': '192.168.1.10',
    'username': 'admin',
    'password': 'password',
}

try:
    net_connect = ConnectHandler(**device)
    net_connect.send_command("terminal length 0")
    output = net_connect.send_command("show running-config")

    hostname = net_connect.find_prompt().strip('#')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"{hostname}_{timestamp}.txt"

    with open(filename, 'w') as f:
        f.write(output)

    print(f"Nexus Backup successful! Saved to {filename}")

except Exception as e:
    print(f"Error: {e}")
finally:
    net_connect.disconnect()