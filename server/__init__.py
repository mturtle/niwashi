from flask import Flask
import shelve


db_path = "devices.db"

app = Flask(__name__)
from server import routes

app.run(host = '0.0.0.0', port=5000, debug=True)
