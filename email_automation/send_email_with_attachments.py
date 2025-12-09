import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

smtp_server = "smtp.yourdomain.com"
smtp_port = 587
username = "your_email@yourdomain.com"
password = "password"

from_addr = "your_email@yourdomain.com"
to_addr = "recipient@example.com"
subject = "Email with Attachments"
body = "Please find attached files."

# Files to attach
files = ["report.pdf", "graph.png"]

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

for file in files:
    try:
        with open(file, "rb") as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={file}')
        msg.attach(part)
    except Exception as e:
        print(f"Error attaching {file}: {e}")

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    print("Email with attachments sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()