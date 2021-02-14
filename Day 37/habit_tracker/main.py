import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "rg42ea5gtr3h4gu1&e14n5u3e"
USERNAME = "jeanbi"
GRAPH_ID = "graph1"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)


GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? ")
}

# response = requests.post(url=PIXEL_ENDPOINT, json=pixel_config, headers=headers)
# print(response.text)

UPDATE_ENDPOINT = f"{PIXEL_ENDPOINT}/20210214"

update_pixel_config = {
    "quantity": "50"
}

# response = requests.put(url=UPDATE_ENDPOINT, json=update_pixel_config, headers=headers)
# print(response.text)


DELETE_ENDPOINT = f"{PIXEL_ENDPOINT}/20210214"

response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
print(response.text)