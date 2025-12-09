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
    lines = net_connect.send_command("show users").splitlines()

    for line in lines[1:]:
        if line.strip():
            vty = line.split()[0]
            try:
                net_connect.send_command(f"clear line {vty}")
                print(f"Cleared line {vty}")
            except:
                print(f"Cannot clear line {vty}")

except Exception as e:
    print(f"Error: {e}")
finally:
    net_connect.disconnect()