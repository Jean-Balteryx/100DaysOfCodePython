import requests
from flight_data import FlightData
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "kaK8qRY2QrfFvaRDC9SlOu9N_E-yMpiT"
LOCATIONS_ENDPOINT = f"{TEQUILA_ENDPOINT}/locations/query"
SEARCH_ENDPOINT = f"{TEQUILA_ENDPOINT}/v2/search"

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.headers = {
            "apiKey": TEQUILA_API_KEY
        }

    def get_iata(self, city_name):
        parameters = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "airport",
            "limit": 1,
            "active_only": "true"
        }

        response = requests.get(url=LOCATIONS_ENDPOINT, params=parameters, headers=self.headers)
        response.raise_for_status()
        return response.json()["locations"][0]["city"]["code"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        data = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=SEARCH_ENDPOINT,
            headers=self.headers,
            params=data,
        )
        try:
            data = response.json()["data"][0]
        except IndexError:
            data["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=self.headers,
                params=data,
            )
            data = response.json()["data"][0]
            pprint(data)
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data
