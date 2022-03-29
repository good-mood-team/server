from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, support_credentials=True)

BASE_ROUTE = "/api"


@app.route(f"{BASE_ROUTE}/getUserStats", methods=["POST"])
def getUserStats():
    data = request.get_json()
    return data


if __name__ == "__main__":
    app.run(debug=True)
