import requests

def client():
    tokenness = "Token a1574b25c8bffbd0e91c673603292182fa8dc68e"
    # credentials = { 'username': 'waffle', 'password': '123' }

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)

    headers = {"Authorization": tokenness}

    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print('Status Code: ', response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()