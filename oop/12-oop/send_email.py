import smtplib, ssl
import os
from config import SENDER, RECEIVER, PASSWORD


class Email:
    def send(self, message):
        host = "smtp.gmail.com"
        port = 465
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(SENDER, PASSWORD)
            server.sendmail(SENDER, RECEIVER, message)
