from flask import Flask, request, jsonify # type: ignore

app = Flask(__name__)

posts = [
    {"id": 1, "title": "Prima postare", "body": "Aceasta este o postare existentă", "userId": 1}
]
next_id = 2

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/posts', methods=['POST'])
def create_post():
    global next_id
    new_post = request.json
    new_post["id"] = next_id
    next_id += 1
    posts.append(new_post)
    return jsonify(new_post), 201

if __name__ == "__main__":
    app.run(debug=True)
