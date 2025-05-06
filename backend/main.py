from flask import request, jsonify
from config import app, db

groceries = ()

@app.route('/')
def home():
    return "Your Flask backend is working!"


@app.route("/groceries", methods = ["GET"])
def get_groceries():
    return jsonify(groceries)

@app.route("/groceries", methods = ["POST"])
def add_grocery():
    data = request.get_json()
    groceries.append(data)
    return jsonify[{"message": "Grocery added", "data": data}], 201


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)

