import json, requests
url = "http://127.0.0.1:5000/posts"

n=int(input("ce id vrei?\n"))
new_post = {
    "title": f"Postare nouă din POST{n}.py",
    "body": "Aceasta este o postare creată folosind un script POST.",
    "userId": n
}

response = requests.post(url, json=new_post)
if response.status_code == 201:
    print("resursa creata cu POST: ", response.json())
else:
    print("error code: ", response.status_code)





# import json
# import requests


# new_post ={
#     "title": "Postare noua",
#     "body": "Aceasta este o postare noua printr un request POST",
#     "userID": 1
# }

# response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
# data=response.json()
# if response.status_code == 201:
#     print("Postare creata cu succes")
#     with open('response.json', 'w') as file:
#             json.dump(data, file, indent=4)
# else:
#       print("Error_code ", response.status_code)

# # 2. Obține toate postările existente (inclusiv cea nouă)
# all_posts_response = requests.get("https://jsonplaceholder.typicode.com/posts")

# if all_posts_response.status_code == 200:
#     all_posts = all_posts_response.json()
#     # Salvează toate postările într-un fișier
#     with open('all_posts.json', 'w') as file:
#         json.dump(all_posts, file, indent=4)
#     print("Toate postările au fost salvate în 'all_posts.json'")
# else:
#     print("Eroare la obținerea tuturor postărilor:", all_posts_response.status_code)