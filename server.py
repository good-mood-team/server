import repackage

repackage.up()

from flask import Flask, request
from flask_cors import CORS

from utils.getMusics import getMusicInfos
from model.model import run_model, init_emotion

app = Flask(__name__)
CORS(app, support_credentials=True)

init_emotion(model="./model/emotion-ferplus-8.onnx")


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
                "videoId": getMusicInfos(genre),
            }
        )

    return res


if __name__ == "__main__":
    app.run(debug=True)
