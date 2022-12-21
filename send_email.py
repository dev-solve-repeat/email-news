import smtplib
import ssl
import os


def send_emails(message):
    port = 465
    host = "smtp.gmail.com"

    username = "dev.solve.repeat@gmail.com"
    password = os.getenv("NEW-PASSWORD")
    receiver = "dev.solve.repeat@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
