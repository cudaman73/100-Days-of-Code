from data_manager import DataManager
from notification_manager import NotificationManager
from flight_data import FlightData
from flight_search import FlightSearch

data = DataManager()
search = FlightSearch()
flight_data = FlightData()
notify_manager = NotificationManager()

for x in data.dest_cities:
    flights = search.get_cheapest_flights(x)
    for flight in flights:
        if flight_data.is_flight_cheaper(flight["price"], data.lowest_prices[x]):
            notify_manager.notify(
                flight['cityFrom'],
                flight['cityTo'],
                flight['flyFrom'],
                flight['flyTo'],
                flight['route'][0]['local_departure'][0:10],
                flight['route'][-1]['local_departure'][0:10],
                flight['price'],
            )
            data.update_sheets(flight['cityTo'], flight['price'])
            break
