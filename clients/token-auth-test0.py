import requests

def client():
    # data = {
    #     'username': "escargot",
    #     'email': "michkail@pm.me",
    #     'password1': "slurpkimochi",
    #     'password2': "slurpkimochi"
    # }

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", data=data)

    tokenness = "Token 4954b9c8e62ed686ddc5613c747ab96fd4290997"
    headers = {"Authorization": tokenness}

    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print('Status Code: ', response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()