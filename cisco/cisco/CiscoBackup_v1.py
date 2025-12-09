from netmiko import ConnectHandler
from datetime import datetime

with open('CiscoBackupIP.txt') as f:
    devices_ip = [line.strip() for line in f if line.strip()]

username = 'admin'
password = 'aaaaaaaa'
secret = 'aaaaaaaa'

for ip in devices_ip:
    device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': username,
        'password': password,
        'secret': secret,
    }
    try:
        net_connect = ConnectHandler(**device)
        net_connect.enable()
        output = net_connect.send_command("show running-config")

        hostname = net_connect.find_prompt().strip('#')
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"{hostname}_{timestamp}.txt"

        with open(filename, 'w') as f:
            f.write(output)

        print(f"[{ip}] Backup successful!")

    except Exception as e:
        print(f"[{ip}] Error: {e}")
    finally:
        net_connect.disconnect()