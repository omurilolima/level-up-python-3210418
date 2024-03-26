import smtplib

SENDER_EMAIL = "MY_EMAIL@EMAIL.COM"  # replace with your email address
SENDER_PASSWORD = "MY_PASSWORD"

def send_email(receiver_email, subject, body):
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP('aspmx.l.google.com', 25) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)

send_email('RECEIVER@EMAIL.COM', 'Notification', 'Everything is working!!!')
