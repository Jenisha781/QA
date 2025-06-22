import requests
import json

url = "https://reqres.in/api/users/2"
headers = {
    "x-api-key": "reqres-free-v1",
    }
data = {
    "name": "Jenisha Updated",
    "job": "Senior QA Engineer"
}

response = requests.put(url, headers=headers, json=data)
assert response.status_code == 200
print("Status Code:", response.status_code)
print("Response:", json.dumps(response.json(), indent=4))
