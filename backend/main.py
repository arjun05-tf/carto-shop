from flask import request, jsonify
from config import app, db
from models import Grocery

@app.route('/')
def home():
    return "Your Flask backend is working!"

@app.route("/groceries", methods=["GET"])
def get_groceries():
    groceries = Grocery.query.all()
    return jsonify([g.to_dict() for g in groceries])

@app.route("/groceries", methods=["POST"])
def add_grocery():
    data = request.get_json()
    new_grocery = Grocery(name=data["name"])
    db.session.add(new_grocery)
    db.session.commit()
    return jsonify({"message": "Grocery added", "data": new_grocery.to_dict()}), 201


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)

