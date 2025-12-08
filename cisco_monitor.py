import paramiko
import time
from datetime import datetime

DEVICE_IP = "192.168.1.1"
USERNAME = "admin"
PASSWORD = "admin123"

CPU_COMMAND = "show processes cpu | include one minute"
INTERFACE_COMMAND = "show ip interface brief"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print("[+] Connecting to device for monitoring...")
    ssh.connect(DEVICE_IP, username=USERNAME, password=PASSWORD, timeout=10)

    shell = ssh.invoke_shell()

    shell.send("terminal length 0\n")
    time.sleep(1)

    shell.send(CPU_COMMAND + "\n")
    time.sleep(2)
    cpu_output = shell.recv(9999).decode()

    shell.send(INTERFACE_COMMAND + "\n")
    time.sleep(2)
    interface_output = shell.recv(9999).decode()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("monitor_log.txt", "a") as logfile:
        logfile.write(f"\n===== {now} =====\n")
        logfile.write("CPU STATUS:\n")
        logfile.write(cpu_output)
        logfile.write("\nINTERFACE STATUS:\n")
        logfile.write(interface_output)

    print("[+] Monitoring data saved to monitor_log.txt")

except Exception as e:
    print("[-] Error:", e)

finally:
    ssh.close()
