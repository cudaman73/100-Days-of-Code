from config import *
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_array = []
        self.url = SHEETY_URL
        self.dest_cities = []
        self.get_destinations()
        self.lowest_prices = {x['iataCode']: x['lowestPrice'] for x in self.destination_array}

    def get_destinations(self):
        response = requests.get(url=self.url, headers={"Authorization": f"Bearer {SHEETY_TOKEN}"})
        response.raise_for_status()
        self.destination_array = response.json()["prices"]
        self.dest_cities = [x['iataCode'] for x in self.destination_array]

    def update_sheets(self, destination, price):
        for x in self.destination_array:
            if x['city'] == destination:
                json = {
                    "price": {
                        "city": x['city'],
                        "iataCode": x['iataCode'],
                        "lowestPrice": price
                    }
                }
                response = requests.put(url=f'{self.url}/{x["id"]}', headers={"Authorization": f"Bearer {SHEETY_TOKEN}"}
                                        , json=json)
                response.raise_for_status()
