import paramiko
import time
from datetime import datetime

USERNAME = "admin"
PASSWORD = "admin123"
ENABLE_PASSWORD = "enable123"

COMMAND = "show running-config"

with open("devices.txt") as f:
    devices = f.read().splitlines()

for ip in devices:
    print(f"[+] Connecting to {ip}")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(ip, username=USERNAME, password=PASSWORD, timeout=10)
        shell = ssh.invoke_shell()

        shell.send("enable\n")
        shell.send(ENABLE_PASSWORD + "\n")
        shell.send("terminal length 0\n")
        shell.send(COMMAND + "\n")

        time.sleep(3)
        output = shell.recv(999999).decode()

        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"backup_{ip}_{now}.txt"

        with open(filename, "w") as backup_file:
            backup_file.write(output)

        print(f"[+] Backup saved for {ip}")

    except Exception as e:
        print(f"[-] Failed on {ip}:", e)

    finally:
        ssh.close()
