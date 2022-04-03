import repackage

repackage.up()

from flask import Flask, request
from flask_cors import CORS
from utils.getMusics import getMusicInfos

app = Flask(__name__)
CORS(app, support_credentials=True)

BASE_ROUTE = "/api"


@app.route(f"{BASE_ROUTE}/getUserStats", methods=["POST"])
def getUserStats():
    data = request.get_json()
    return data


@app.route(f"{BASE_ROUTE}/getYoutubeUrl", methods=["POST"])
def getYoutubeUrl():
    data = request.get_json()

    res = {"tracks": []}

    for genre in data["genres"]:
        res["tracks"].append(
            {
                "genre": genre,
                "url": "https://youtube.com/clip/Ugkx5i8TnLeMZdY6w6SYH1xcnn_d2QDrFm2c"
                # "url": getMusicInfos(genre)
            }
        )

    return res


if __name__ == "__main__":
    app.run(debug=True)
