from pprint import pprint
import requests
from config import *


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=f'{SHEETY_URL}/prices', headers={'Authorization': f'Bearer {SHEETY_TOKEN}'})
        data = response.json()
        with open("response.json", "w") as file:
            file.write(response.json())
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_URL}/prices/{city['id']}",
                json=new_data
            )
            print(response.text)
