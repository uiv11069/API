import requests

# ID-ul postării pe care vrem să o ștergem
post_id = int(input("ce id vrei sa stergi?\n"))

# URL-ul endpoint-ului DELETE
url = f"http://127.0.0.1:5000/posts/{post_id}"

# Trimite cererea DELETE către server
response = requests.delete(url)

# Verifică răspunsul
if response.status_code == 200:
    print("Postare ștearsă cu succes:")
    print(response.json())  # Mesaj de confirmare
else:
    print(f"Eroare: {response.status_code}")
    print(response.text)
