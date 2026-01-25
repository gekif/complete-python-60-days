import smtplib
import ssl
from email.message import EmailMessage
from config import USER_EMAIL, USER_PASSWORD


def send_email(subject: str, body: str, to_email: str = USER_EMAIL):
    host = "smtp.gmail.com"
    port = 465

    # ===== BUILD EMAIL (RFC 5322 COMPLIANT) =====
    msg = EmailMessage()
    msg["From"] = USER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(USER_EMAIL, USER_PASSWORD)
        server.send_message(msg)
