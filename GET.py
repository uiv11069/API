import requests, json


# URL-ul endpoint-ului GET
url = "http://127.0.0.1:5000/posts"

# Trimite cererea GET
response = requests.get(url)

# Verifică răspunsul
if response.status_code == 200:
    print("Postările existente:")
    with open('response.json', 'w') as file:
        json.dump(response.json(), file, indent=4)
    print(response.json())
else:
    print(f"Eroare: {response.status_code}")













# from http.client import responses
# from builtins import open, print # type: ignore
# import json
# import requests
# response =requests.get("https://jsonplaceholder.typicode.com/posts/1")
# data = response.json()
# if response.status_code == 200:
#     data = response.json()
#     print("Titlul postării:", data['title'])
#     with open('response.json', 'w') as file:
#         json.dump(data, file, indent=4)
# else:
#     print("Eroare:", response.status_code)


