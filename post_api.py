import requests
import json

url = "https://reqres.in/api/users"
headers = {
    "x-api-key": "reqres-free-v1",
    "Content-Type": "application/json"
}
data = {
    "name": "Jenisha",
    "job": "QA Engineer"
}

response = requests.post(url, headers=headers, json=data)
assert response.status_code == 201
print("Status Code:", response.status_code)
print("Response:", json.dumps(response.json(), indent=4))


