import smtplib
from django.conf import settings

def smtp_login():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(f"{settings.EMAIL_HOST_USER}", f"{settings.EMAIL_HOST_PASSWORD}")
    server.ehlo()