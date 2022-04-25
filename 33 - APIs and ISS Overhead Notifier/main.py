import requests
from datetime import datetime
from config import *
import smtplib
from math import isclose


def iss_in_range(lat, long):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Here I used the math.isclose function to check relative values instead of doing
    # value1 <= lat <= value2 because I feel like it's more elegant
    return isclose(lat, iss_latitude, abs_tol=5) and isclose(long, iss_longitude, abs_tol=5)


def is_dark(lat, long):
    parameters = {
        "lat": lat,
        "lng": long,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.utcnow().hour
    return sunset <= time_now <= sunrise


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if iss_in_range(MY_LAT, MY_LONG) and is_dark(MY_LAT, MY_LONG):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=app_key)
        connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject:ISS overhead!\n\nLook up!")
    print("ISS is overhead!")
else:
    print("ISS not overhead or it's not dark, sorry bro.")
