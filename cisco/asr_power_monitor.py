from netmiko import ConnectHandler

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

    output = net_connect.send_command("show environment power")
    lines = output.splitlines()

    for line in lines:
        if "Fail" in line or "Offline" in line:
            print("ALERT:", line)

except Exception as e:
    print(f"Error: {e}")
finally:
    net_connect.disconnect()