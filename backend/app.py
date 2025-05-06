from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
DATABASE = "groceries.db"

#Database config
app.config("")

groceries = ()

if __name__ == '__main__':
    app.run(debug=True)