from twilio.rest import Client
from config import *
import smtplib


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)
        self.email_from = FROM_EMAIL
        self.smtp_key = SMTP_KEY

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=FROM_PHONE,
            to=TO_PHONE,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_email(self, message, to_email):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email_from, password=self.smtp_key)
            connection.sendmail(from_addr=self.email_from, to_addrs=to_email, msg=message)
