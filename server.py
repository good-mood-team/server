import repackage

repackage.up()

from flask import Flask, request
from flask_cors import CORS

from utils.getMusics import getMusicInfos
from model.model import run_model, init_emotion

app = Flask(__name__)
CORS(app, support_credentials=True)

init_emotion(model="./model/emotion-ferplus-8.onnx")


@app.before_request
def handle_chunking():
    """
    Sets the "wsgi.input_terminated" environment flag, thus enabling
    Werkzeug to pass chunked requests as streams.  The gunicorn server
    should set this, but it's not yet been implemented.
    """

    transfer_encoding = request.headers.get("Transfer-Encoding", None)
    if transfer_encoding == u"chunked":
        request.environ["wsgi.input_terminated"] = True


@app.route("/", methods=["GET"])
def index() -> str:
    return "Hello World!"

@app.route("/getUserStats", methods=["POST"])
def getUserStats() -> dict:
    data = request.get_json()

    res = run_model(data)

    return res


@app.route("/getYoutubeUrl", methods=["POST"])
def getYoutubeUrl() -> dict:
    data = request.get_json()

    res = {"tracks": []}

    import random

    testIds = ["sI2U3zjKeYU", "lB8uQ_zO-o8", "key_vfp10Yw", "iX-QaNzd-0Y", "GCdwKhTtNNw"]

    for genre in data["genres"]:
        res["tracks"].append(
            {
                "genre": genre,
                # "videoId": testIds[random.randint(0, len(testIds) - 1)]
                "videoId": getMusicInfos(genre),
            }
        )

    return res


if __name__ == "__main__":
    app.run(debug=True)
