import requests
post_id=3

url="http://127.0.0.1:5000/posts/3"

partial_update = {
    "title": "Titlu actualizat cu PATCH.py"
}

response= requests.patch(url, json=partial_update)

if response.status_code == 200:
    print("Postare actualizată cu succes:")
    print(response.json())
else:
    print(f"Eroare: {response.status_code}")
    print(response.text)