#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

from config import *
from datetime import datetime, timedelta
from data_manager import *
from sheets import destination_array
import requests
import json
import notification_manager
from flight_data import FlightData
from flight_search import FlightSearch

data = DataManager()
dest_cities = ""


dest_cities_2 = "PAR,BER,TYO,SYD,IST,KUL,NYC,SFO,CPT,LON"


# flight_search = FlightSearch(dest_cities)
#
# flight_data = flight_search.get_cheapest_flights()

