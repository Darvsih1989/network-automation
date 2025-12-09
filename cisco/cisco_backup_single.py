from netmiko import ConnectHandler
from datetime import datetime

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
    'secret': 'enablepassword',
}

try:
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    output = net_connect.send_command("show running-config")

    hostname = net_connect.find_prompt().strip('#')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"{hostname}_{timestamp}.txt"

    with open(filename, "w") as f:
        f.write(output)

    print(f"Backup successful! Saved to {filename}")

except Exception as e:
    print(f"Error: {e}")

finally:
    net_connect.disconnect()