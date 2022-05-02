from config import *
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.sid = TWILIO_SID
        self.token = TWILIO_TOKEN
        self.to_phone = TO_PHONE
        self.from_phone = FROM_PHONE

    def notify(self, from_city, to_city, from_iata, to_iata, depart_date, return_date, price):
        # send to to_phone via twilio API
        client = Client(self.sid, self.token)
        message = client.messages \
            .create(
                body=f"Low price alert! Only ${price} to fly from {from_city}-{from_iata} to {to_city}-{to_iata}, "
                     f"from {depart_date} to {return_date}.",
                from_=f"{self.from_phone}",
                to=f"{self.to_phone}"
            )

        # print the message in case we need to save it
        print(message.sid)
