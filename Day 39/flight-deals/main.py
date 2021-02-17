from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

# Origin city
ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Retrieves google sheets rows
sheet_data = data_manager.retrieve_data()

# Adds IATA codes if necessary
if sheet_data[0]["iataCode"] == "":
    for city in sheet_data:
        city["iataCode"] = flight_search.get_iata(city["city"])

    data_manager.destinations = sheet_data
    data_manager.update_data()

# Computes dates to search for
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    # Checks for flights
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    # # Send SMS if price is lower
    if flight is not None and flight.price < destination["lowestPrice"]:
        users = data_manager.get_emails()
        emails = [row["email"] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from " \
               f"{flight.origin_city}-{flight.origin_airport} to " \
               f"{flight.destination_city}-{flight.destination_airport}, " \
               f"from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"Flight has {flight.stop_overs}, via {flight.via_city}."

        notification_manager.send_alert(message)

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        notification_manager.send_emails(emails, message, link)
