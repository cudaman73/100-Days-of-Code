from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from config import SHEET_DATA, USER_DATA

data_manager = DataManager()
# sheet_data = data_manager.get_destination_data()
# user_data = data_manager.get_user_data()
sheet_data = SHEET_DATA
user_data = USER_DATA
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "AUS"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:

    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        message = f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stopovers != 0:
            message += f"\n Flight has 1 stopover, via {flight.via_city}"

        for user in user_data:
            email_message = "Subject: New Low Price Flight!\n\n" + message + f"\nhttps://www.google.com/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
            notification_manager.send_email(email_message, user['email'])
        # notification_manager.send_sms(message)
