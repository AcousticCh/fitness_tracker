import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

query = input("Todays workout?\n")
NUTRI_ENDPOINT = os.environ.get("NUTRI_ENDPOINT")
NUTRI_ID = os.environ.get("NUTRI_ID")
NUTRI_API_KEY = os.environ.get("NUTRI_API_KEY")
HEADER = {
    "x-app-id": NUTRI_ID,
    "x-app-key": NUTRI_API_KEY
}

NUTRI_PARAMS = {
    "query": query,
    "gender": "male",
    "weight_kg": 65.7,
    "height_cm": 180.3,
    "age": 24
}

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_API_KEY = os.environ.get("SHEETY_API_KEY")
SHEETY_HEADER = {
    "Authorization": SHEETY_API_KEY
}

# for each exercise add sheety row
date = f"{datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}"
nutri_response = requests.post(url=NUTRI_ENDPOINT, headers=HEADER, json=NUTRI_PARAMS)
print(nutri_response.json())
for i in nutri_response.json()["exercises"]:
    exercise = str(i["name"].title())
    length = int(i["duration_min"])
    burned_calories = int(i["nf_calories"])
    sheety_input = {
        "workout": {
            "date": date,
            "time": f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}",
            "exercise": exercise,
            "duration": length,
            "calories": burned_calories
        }
    }
    sheety_post = requests.post(url=SHEETY_ENDPOINT, headers=SHEETY_HEADER, json=sheety_input)
    sheety_post.raise_for_status()
    print(sheety_post.json())

#
#
#
#