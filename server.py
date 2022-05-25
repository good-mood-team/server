import os
import sys
import json

import repackage

repackage.up()

from flask import Flask, request
from flask_cors import CORS

from utils.getMusics import getMusicInfos
from model.model import run_model, init_emotion

app = Flask(__name__)
CORS(app, support_credentials=True)

init_emotion(model="./model/emotion-ferplus-8.onnx")

if not os.path.isfile("credentials.json"):
    sys.exit("'credentials.json' not found! Please add it and try again.")
else:
    with open("credentials.json") as file:
        credentials = json.load(file)

API_KEY = credentials["API_KEY"]


@app.route("/", methods=["GET"])
def index() -> str:
    return "Backend is running!"


@app.route("/getUserStats", methods=["POST"])
def getUserStats() -> dict:

    data = request.get_json()

    res = run_model(data)

    return {"payload_size": f"{request.content_length / 10**6} Mb", "emotions": res}


@app.route("/getYoutubeUrl", methods=["POST"])
def getYoutubeUrl() -> dict:
    data = request.get_json()

    res = {"tracks": []}

    for genre in data["genres"]:
        res["tracks"].append(
            {
                "genre": genre,
                "videoId": "Ux5cQbO_ybw"
                # "videoId": getMusicInfos(genre, API_KEY),
            }
        )

    return res


if __name__ == "__main__":
    app.run(debug=True)
