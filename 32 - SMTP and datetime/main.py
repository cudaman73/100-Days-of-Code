import csv
import datetime as dt
import smtplib
from account_data import *
from random import choice
from os import listdir
from os.path import isfile, join

letters = [f for f in listdir("letter_templates") if isfile(join("letter_templates", f))]
birthdays = []


def send_email(name):
    with open(f"letter_templates/{choice(letters)}") as letter:
        data = letter.read()

    data = data.replace('[NAME]', name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=app_key)
        connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject:Happy Birthday!\n\n{data}")


with open(file="birthdays.csv") as file:
    csv = csv.DictReader(file)
    for _ in csv:
        birthdays.append(_)

today = dt.datetime.now()

for _ in birthdays:
    if _['month'] == str(today.month) and _['day'] == str(today.day):
        send_email(_['name'])