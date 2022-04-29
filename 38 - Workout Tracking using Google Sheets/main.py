from config import *
import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = "181"
HEIGHT_CM = "71"
AGE = "34"
EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_URL = "https://api.sheety.co/cfd0099d0116189cd0a6cc72aa2382d6/myWorkouts/workouts"
now_date = datetime.now().strftime("%Y-%m-%d")
now_time = datetime.now().strftime("%H:%M:%S")

headers = {
    "x-app-id": f"{APP_ID}",
    "x-app-key": f"{API_KEY}"
}

params = {"query": f"{input('What exercise for what duration?')}",
          "gender": GENDER,
          "weight_kg": WEIGHT_KG,
          "height_cm": HEIGHT_CM,
          "age": AGE}

response = requests.post(url=EXERCISE_URL, headers=headers, data=params)
response.raise_for_status()

data = response.json()["exercises"]

for x in data:

    workout_data = {
        "workout": {
            "date": now_date,
            "time": now_time,
            "exercise": x["user_input"],
            "duration": str(x["duration_min"]),
            "calories": x["nf_calories"]
        }
    }
    sheety_response = requests.post(url=SHEETY_URL, json=workout_data, headers={"Authorization": f"Bearer "
                                                                                                 f"{SECRET_TOKEN}"})
    sheety_response.raise_for_status()

    print(sheety_response.text)
