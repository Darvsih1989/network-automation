import paramiko
from datetime import datetime

# Device information
DEVICE_IP = "192.168.1.1"
USERNAME = "admin"
PASSWORD = "admin123"
ENABLE_PASSWORD = "enable123"

# Command to run
COMMAND = "show running-config"

# Create SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print("[+] Connecting to device...")
    ssh.connect(DEVICE_IP, username=USERNAME, password=PASSWORD, timeout=10)

    shell = ssh.invoke_shell()
    shell.send("enable\n")
    shell.send(ENABLE_PASSWORD + "\n")
    shell.send("terminal length 0\n")
    shell.send(COMMAND + "\n")

    import time
    time.sleep(3)

    output = shell.recv(65535).decode()

    # Create backup file
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"backup_{DEVICE_IP}_{now}.txt"

    with open(filename, "w") as file:
        file.write(output)

    print(f"[+] Backup saved as {filename}")

except Exception as e:
    print("[-] Error:", e)

finally:
    ssh.close()
