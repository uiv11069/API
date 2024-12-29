from flask import Flask, request, jsonify # type: ignore

app = Flask(__name__)

# Listă în memorie pentru a stoca postările
posts = [
    {"id": 1, "title": "Prima postare", "body": "Aceasta este o postare existentă", "userId": 1}
]
next_id = 2  # Pentru generarea de ID-uri unice

# GET: Obține toate postările
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts), 200

# GET: Obține o singură postare pe baza ID-ului
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    for post in posts:
        if post['id'] == post_id:
            return jsonify(post), 200
    return jsonify({"error": "Postare nu a fost găsită"}), 404

# POST: Creează o postare nouă
@app.route('/posts', methods=['POST'])
def create_post():
    global next_id
    new_post = request.json
    if not new_post.get("title") or not new_post.get("body"):
        return jsonify({"error": "Câmpurile 'title' și 'body' sunt necesare"}), 400

    new_post["id"] = next_id
    next_id += 1
    posts.append(new_post)
    return jsonify(new_post), 201

# PUT: Actualizează complet o postare pe baza ID-ului
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    updated_post = request.json
    for post in posts:
        if post['id'] == post_id:
            post.update(updated_post)
            return jsonify(post), 200
    return jsonify({"error": "Postare nu a fost găsită"}), 404

# PATCH: Actualizează parțial o postare pe baza ID-ului
@app.route('/posts/<int:post_id>', methods=['PATCH'])
def patch_post(post_id):
    partial_update = request.json
    for post in posts:
        if post['id'] == post_id:
            post.update(partial_update)
            return jsonify(post), 200
    return jsonify({"error": "Postare nu a fost găsită"}), 404

# DELETE: Șterge o postare pe baza ID-ului
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    for post in posts:
        if post['id'] == post_id:
            posts = [p for p in posts if p['id'] != post_id]
            return jsonify({"message": "Postare ștearsă"}), 200
    return jsonify({"error": "Postare nu a fost găsită"}), 404

# Error handler pentru pagini inexistente
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resursa nu a fost găsită"}), 404

if __name__ == "__main__":
    app.run(debug=True)
