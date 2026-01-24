import smtplib, ssl
from config import USER_EMAIL, USER_PASSWORD

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = USER_EMAIL
    password = USER_PASSWORD

    receiver = USER_EMAIL
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)