import requests
from datetime import datetime

APP_ID = "f78327f9"
API_KEY = "a5f94da6e46a770506de8d1c103155ce"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

parameters = {
    "query": input("Tell me which exercise you did: "),
    "gender": "male",
    "weight_kg": 90,
    "height_cm": 195,
    "age": 25
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()
exercises = response.json()["exercises"]

SHEET_ENDPOINT = "https://api.sheety.co/bba15cc89b5c4ff0ff1da589fdb5218c/workoutTracking/workouts"

headers = {
    "Authorization": "Bearer secrettoken"
}

today = datetime.now()

for exercise in exercises:
    parameters = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=SHEET_ENDPOINT, json=parameters, headers=headers)
    response.raise_for_status()
