from config import *
import requests
from datetime import datetime, timedelta
import json


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, destination):
        self.url = TEQUILA_URL
        self.home = "AUS"
        self.dest = destination

    def get_cheapest_flights(self):
        params = {
            "fly_from": "AUS",
            "fly_to": self.dest,
            "date_from": f"{datetime.now().strftime('%d/%m/%Y')}",
            "date_to": f'{(datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")}',
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 14,
            "flight_type": "round",
            "only_working_days": False,
            "only_weekends": False,
            "curr": "USD",
            "locale": "en",
            "max_stopovers": 2,
            "limit": 200
        }
        response = requests.get(url=TEQUILA_URL, headers=TEQUILA_HEADER, params=params)
        response.raise_for_status()
        return response.json()["data"]
