import requests
question_data = []


def get_data():
    parameters = {
        "amount": 10,
        "category": 9,
        "type": "boolean"
    }

    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    return response.json()["results"]
