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
    return jsonify(users)

    

if __name__ == "__main__":
    app.run(debug=True)