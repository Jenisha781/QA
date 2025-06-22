import requests
import json

url = "https://reqres.in/api/users/2"
headers = {
    "x-api-key": "reqres-free-v1",
    "Content-Type": "application/json"
}
data = {
    "job": "Lead QA Engineer"
}

response = requests.patch(url, headers=headers, json=data)
print("Status Code:", response.status_code)
print("Response:", json.dumps(response.json(), indent=4))
