#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

from config import *
from data_manager import *
import notification_manager
import flight_data
import flight_search

cities = DataManager()

print(cities.destination_array)
