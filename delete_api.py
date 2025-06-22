import requests
import json

api = "https://reqres.in/api/users/2"
headers = {
    "x-api-key": "reqres-free-v1",
    "Content-Type": "application/json"
}
def del_user():
    response = requests.delete(api, headers=headers)
    assert response.status_code == 204
    print("Status Code:", response.status_code)

del_user()    
    

