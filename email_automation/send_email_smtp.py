import smtplib
from email.mime.text import MIMEText

# Email details
smtp_server = "smtp.yourdomain.com"
smtp_port = 587
username = "your_email@yourdomain.com"
password = "password"

from_addr = "your_email@yourdomain.com"
to_addr = "recipient@example.com"
subject = "Test Email"
body = "Hello! This is a test email."

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = from_addr
msg['To'] = to_addr

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()