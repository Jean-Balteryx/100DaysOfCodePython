import requests
from datetime import datetime

MY_LAT = 47.218372
MY_LNG = -1.553621

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LNG}")
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)


time_now = datetime.now()

print(time_now.hour)