import requests
import json

url = "https://httpbin.org/post"
headers = {
    "Content-Type": "application/json"
}

data = {
    "name": "natalia"
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()

    if response.status_code == 200:
        response_data = response.json()
        print(response_data)

except requests.exceptions.HTTPError as err:
    print("Wystąpił błąd HTTP:", err)

except requests.exceptions.RequestException as err:
    print("Wystąpił ogólny błąd:", err)
