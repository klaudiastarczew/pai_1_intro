import requests
import jmespath

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    members = data.get("members", [])
    for member in members:
        print(member.get("name"))

    for j in range(len(members)):
        search_expression = f"members[{j}].name"
        print(jmespath.search(search_expression, data))

except requests.exceptions.RequestException as err:
    print("Wystąpił błąd:", err)
