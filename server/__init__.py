from flask import Flask

print(f"creating app in {__name__}", flush=True)
app = Flask(__name__)
from server import routes

print("flask firing up")
app.run(host = '0.0.0.0', port=5000, debug=True)
