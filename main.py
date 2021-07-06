from flask import Flask, jsonify


#inicializa flask con el nombre main.py
app = Flask(__name__)

users = [
    {
        "Username": "Admin",
        "Age": "25",
    },
    {
        "Username": "User 1",
        "Age": "18",
    }
]

@app.route('/users', methods=["GET"])
def getAllUsers():
    return jsonify(users), 200


@app.route('/users/<string:username>', methods=["GET"])
def getUsersByUsername(username):
    result = next((user for user in users if user["Username"] == username), None)
    if result is not None:
        return jsonify(result), 200
    else:
        return "User not found", 404


if __name__ == "__main__":
    app.run(debug=True)