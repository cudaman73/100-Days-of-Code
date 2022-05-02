from twilio.rest import Client
from config import *




class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send_sms(self, message):
        # message = self.client.messages.create(
        #     body=message,
        #     from_=FROM_PHONE,
        #     to=TO_PHONE,
        # )
        # # Prints if successfully sent.
        # print(message.sid)
        print(message)
