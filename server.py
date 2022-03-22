from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, support_credentials=True)

BASE_ROUTE = "/api"


@app.route(f"{BASE_ROUTE}/receiveVideo")
def receiveVideo():
    return "Video received!"


if __name__ == "__main__":
    app.run()
