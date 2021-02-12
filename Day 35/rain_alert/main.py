import requests
import os
from twilio.rest import Client

# Weather API
# export OWM_API_KEY=fe5931041ba650b6f561b5178f2de565
API_KEY = os.getenv("OWM_API_KEY")
CITY = "Nantes,FR"
MY_LAT = 46.947975
MY_LON = 7.447447
API_URL = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

# Twilio API

ACCOUNT_SID = "ACeb1b8f647238fb1313e69c2ebdd37f50"
# export AUTH_TOKEN=cfc057bd2902defcbcd15a3ac8ed15d5
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
client = Client(ACCOUNT_SID, AUTH_TOKEN)

response = requests.get(url=API_URL, params=parameters)
response.raise_for_status()
print(response.status_code)
data = response.json()

for hour_data in data["hourly"][:12]:
    if hour_data["weather"][0]["id"] < 700:
        message = client.messages \
            .create(
                body="Bring an umbrella.",
                from_="+15863718448",
                to="+33665708618"
        )

        print(message.status)
        break

