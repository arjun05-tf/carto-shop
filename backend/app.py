import sqlite3
from flask import Flask, request, jsonify, g
from datetime import datetime

app = Flask(__name__)
DATABASE = 'groceries.db'

# Connect to the database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

# Close DB connection when done
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Initialize DB + Create Table
def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS grocery (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                unit TEXT NOT NULL,
                category TEXT,
                purchased BOOLEAN DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        db.commit()

# Route to test
@app.route('/')
def home():
    return "Raw SQLite connected!"

# Add item
@app.route('/groceries', methods=['POST'])
def add_item():
    data = request.get_json()
    db = get_db()
    db.execute('''
        INSERT INTO grocery (item_name, quantity, unit, category, purchased)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        data['item_name'],
        data['quantity'],
        data['unit'],
        data.get('category'),
        int(data.get('purchased', False))
    ))
    db.commit()
    return jsonify({"message": "Item added!"}), 201

# Get all items
@app.route('/groceries', methods=['GET'])
def get_items():
    db = get_db()
    cur = db.execute('SELECT * FROM grocery')
    rows = cur.fetchall()
    return jsonify([dict(row) for row in rows])

# Initialize DB once
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
