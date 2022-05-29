import os
import sys
import json
from unittest import result

import repackage

from db.api import add_results, connect

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

conn = connect(host="localhost")
db = conn.gm


@app.route("/", methods=["GET"])
def index() -> str:
    return "Backend is running!"


@app.route("/getUserStats", methods=["POST"])
def getUserStats() -> dict:
    req = request.get_json()

    res = run_model(req["results"])

    payload = {**req, "results": res}

    if res:
        add_results(db, payload)

    return {"payload_size": f"{request.content_length / 10**6} Mb", "emotions": res, "genre": req["genre"]}


@app.route("/getYoutubeUrl", methods=["POST"])
def getYoutubeUrl() -> dict:
    req = request.get_json()

    res = {"status": 200, "tracks": []}

    videoId = None
    # videoId = "U-Z_bZS8t3M"

    for genre in req["genres"]:
        try:
            videoId = getMusicInfos(genre, API_KEY)
        except:
            return {"status": 114, "message": "API rate limit has been exceeded."}

        res["tracks"].append(
            {
                "genre": genre,
                "videoId": videoId,
            }
        )

    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
