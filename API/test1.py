import requests
import json
import faker

faker = faker.Faker()

base_url = input("Enter the base URL for the API: ")

def test_get_users():
    url = base_url + "/api/users"
    response = requests.get(url)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("GET ALL USERS response: ", json_str)

test_get_users()
