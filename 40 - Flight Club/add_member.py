# Basic text interface to get First, Last, and Email from user to be able to send emails with flight deals
import requests
from config import *


def get_email():
    email = input("What is your email?")
    email_confirm = input("Enter email again for confirmation:")
    if email != email_confirm:
        print("Sorry, emails do not match, try again.")
        get_email()
    return email


print("Welcome to Dale's Flight Club\n", "We find the best flight deals and email them to you.")

# first_name =
# last_name =
# user_email =
json = {
            "user": {
                "firstName": input("What is your first name?"),
                "lastName": input("What is your last name?"),
                "email": get_email()
            }
        }

response = requests.post(url=SHEETY_URL, headers={"Authorization": f"Bearer {SHEETY_TOKEN}"}, json=json)
response.raise_for_status()
