import requests

PRICES_ENDPOINT = "https://api.sheety.co/bba15cc89b5c4ff0ff1da589fdb5218c/flightDeals/prices"
USERS_ENDPOINT = "https://api.sheety.co/bba15cc89b5c4ff0ff1da589fdb5218c/flightDeals/users"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destinations = {}
        self.customer_data = {}

    def retrieve_data(self):
        response = requests.get(url=PRICES_ENDPOINT)
        response.raise_for_status()
        self.destinations = response.json()["prices"]
        return self.destinations

    def update_data(self):
        for destination in self.destinations:
            changes = {
                "price": {
                    "iataCode": destination["iataCode"]
                }
            }
            endpoint = f"{PRICES_ENDPOINT}/{destination['id']}"
            response = requests.put(url=endpoint, json=changes)
            response.raise_for_status()

    def get_emails(self):
        response = requests.get(url=USERS_ENDPOINT)
        response.raise_for_status()
        self.customer_data = response.json()["users"]
        return self.customer_data
