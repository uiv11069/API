import requests

# ID-ul postării pe care vrem să o actualizăm
post_id = int(input("ce id vrei sa modifici complet?\n"))

# URL-ul endpoint-ului PUT
url = f"http://127.0.0.1:5000/posts/{post_id}"

# Datele actualizate pentru resursă
updated_post = {
    "id": post_id,  # ID-ul trebuie să rămână același
    "title": "Titlu complet actualizat cu PUT",
    "body": "Acesta este noul conținut complet al postării.",
    "userId": 2
}

# Trimite cererea PUT către server
response = requests.put(url, json=updated_post)

# Verifică răspunsul
if response.status_code == 200:
    print("Postare actualizată cu succes:")
    print(response.json())  # Afișează resursa actualizată
else:
    print(f"Eroare: {response.status_code}")
    print(response.text)
