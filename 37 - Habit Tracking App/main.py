import requests
from config import *
from datetime import datetime

url = "https://pixe.la/v1/users"
graph_url = f"{url}/{USERNAME}/graphs"
graph_id = "test-graph"
date = datetime.now().strftime("%Y%m%d")

request_header = {
    "X-USER-TOKEN": TOKEN
}

params = {
    "date": f"{date}"
}

# response = requests.post(url=url, json=params)
# response.raise_for_status()
# print(response.text)

# this deleted the graph, not the date/pixel i was trying to delete, because i did not read the documentation properly.
response = requests.delete(url=f"{graph_url}/{graph_id}", headers=request_header, json=params)
print(response.text)
