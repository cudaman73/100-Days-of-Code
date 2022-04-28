# config.py contains sensitive API data, and isn't uploaded to github for security reasons.
# it contains the following keys: AV_KEY, NA_KEY, twilio_sid, twilio_key, from_phone, and to_phone
# if you use this code yourself, you will have to populate them appropriately.
from config import *
import re
from datetime import datetime
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TODAY = datetime.today().strftime('%Y-%m-%d')
YESTERDAY = TODAY[:-1] + str(int(TODAY[-1]) - 1)
TWO_DAYS_AGO = TODAY[:-1] + str(int(TODAY[-1]) - 2)
REGEX = re.compile('(<.*?>)')

av_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": f"{STOCK}",
    "interval": "60min",
    "apikey": f"{AV_KEY}"
}

# STEP 1: Use https://www.alphavantage.co to get current stock prices
response = requests.get(url="https://www.alphavantage.co/query", params=av_params)
response.raise_for_status()
av_data = response.json()['Time Series (60min)']

# grab yesterday and the preceding days' closing stock prices and calculate the percentage change
yesterday_price = float(av_data[f"{YESTERDAY} 20:00:00"]["4. close"])
two_day_price = float(av_data[f"{TWO_DAYS_AGO} 20:00:00"]["4. close"])
value_delta = round(yesterday_price / two_day_price * 100 // 1 - 100)

if value_delta >= 5 or value_delta <= -5:

    # use newsapi to grab articles that mention STOCK
    na_params = {
        "q": f"{COMPANY_NAME}",
        "apikey": f"{NA_KEY}"
    }

    news_request = requests.get(url="https://newsapi.org/v2/everything", params=na_params)
    news_request.raise_for_status()
    news_data = []

    # grab the first three articles that mention STOCK
    # slight jank - some article briefs have html, so we use re.sub to strip them for easier readability
    for y in range(0, 3):
        news_title = news_request.json()['articles'][y]['title']
        news_brief = re.sub(REGEX, '', news_request.json()['articles'][y]['description'])

        # send to to_phone via twilio API
        client = Client(twilio_sid, twilio_key)
        message = client.messages \
            .create(
                body=f"{STOCK}: {'🔻' if value_delta < 0 else '🔺'}{value_delta}% Headline: {news_title}. "
                     f"Brief: {news_brief}.",
                from_=f"{from_phone}",
                to=f"{to_phone}"
            )

        # print the message in case we need to save it
        print(message.sid)
