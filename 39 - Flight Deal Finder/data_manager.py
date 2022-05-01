from config import *
import json
import requests
from sheets import destination_array as D_A


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_array = []
        self.url = SHEETY_URL
        self.dest_cities = []
        self.get_destinations()

    def get_destinations(self):
        """TODO: change this back to a API request when finished - modified so we don't run out of API calls to sheety"""
        # response = requests.get(url=self.url, headers={"Authorization": f"Bearer {SHEETY_TOKEN}"})
        # response.raise_for_status()
        # self.destination_array = response.json()["prices"]
        self.destination_array = D_A
        self.dest_cities = ",".join([x['iataCode'] for x in self.destination_array])
        print(self.dest_cities)

