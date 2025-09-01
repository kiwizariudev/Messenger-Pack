import smtplib
from email.mime.text import MIMEText

def send_email(sender, password, receiver, message, smtp="smtp.gmail.com", port=587):
    msg = MIMEText(message)
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = "Python Mail"

    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()
    print("Email sent successfully!")
