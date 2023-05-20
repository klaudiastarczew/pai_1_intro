import requests

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"

try:
    response = requests.get(url)
    response.raise_for_status()

    if response.status_code == 200:
        data = response.json()
        print(data)

except requests.exceptions.HTTPError as err:
    print("Wystąpił błąd HTTP:", err)

except requests.exceptions.RequestException as err:
    print("Wystąpił ogólny błąd:", err)
