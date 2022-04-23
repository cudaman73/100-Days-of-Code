import smtplib
import datetime as dt
from random import choice
from account_data import *

with open("quotes.txt") as file:
    quotes = file.readlines()

daily_quote = choice(quotes)
new_date = dt.datetime.now()

if new_date.weekday() == 0:
    print("It's Monday! Time to send a quote.")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=app_key)
        connection.sendmail(from_addr=email, to_addrs=email, msg="Subject:Monday Morning Motivational Quote!\n\nHello "
                                                                 "Sir. Your monday morning motivational quote is:\n\n "
                                                                 f"{daily_quote}")
else:
    print("Not Monday, did not send email.")