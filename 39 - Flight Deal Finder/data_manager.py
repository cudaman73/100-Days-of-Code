from config import *
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_array = []
        self.get_destinations()
        self.home_IATA = "AUS"

    def get_destinations(self):
        response = requests.get(url=SHEETY_URL, headers={"Authorization": f"Bearer {SHEETY_TOKEN}"})
        response.raise_for_status()
        self.destination_array = response.json()["prices"]
