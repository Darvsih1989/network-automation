from Mikrotik_Connector import Mikrotik
from datetime import datetime

# Device info
router_ip = "192.168.88.1"
username = "admin"
password = "password"

try:
    router = Mikrotik(router_ip, username, password)
    backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M')}.backup"
    
    router.system_backup(name=backup_name)
    print(f"Backup successful! Saved as {backup_name}")

except Exception as e:
    print(f"Error: {e}")
finally:
    router.disconnect()