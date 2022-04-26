import json
import requests
from config import *
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient
# import os


def convert_temp(k_temp):
    return int((k_temp - 273.15) * 9/5 + 32)

hourly_data = []
url = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": f"{MY_LAT}",
    "lon": f"{MY_LONG}",
    "appid": f"{appid}",
    "exclude": "minutely"
}

response = requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()

with open("response.json", "w") as file:
    json.dump(data, file, indent=4)

for x in range(12):
    hourly_data.append(data["hourly"][x]["weather"][0]["main"])

if 'Rain' in hourly_data:
    # proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
    # client = Client(account_sid, account_token, http_client=proxy_client)
    client = Client(account_sid, account_token)
    message = client.messages \
                    .create(
                         body=f"it\'s gonna rain at {hourly_data.index('Rain') + 1}, you should grab an umbrella",
                         from_=f"{from_phone}",
                         to=f"{to_phone}"
                     )
    print(message.sid)
