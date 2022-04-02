import requests as req
import random

API_KEY = "AIzaSyAfHh4ljEXd3de6i5Daw5xG6mtlJYGkThE"
BASE_URL = "https://youtube.googleapis.com/youtube/v3"


def getMusicInfos(genre) -> str:

    r = req.get(
        f"{BASE_URL}/search?maxResults=500&q={genre}%20instrumental&safeSearch=strict&type=video&key={API_KEY}")
    r = r.json()

    # print(r)

    rnd = random.randint(0, len(r["items"])-1)
    item = r["items"][rnd]
    print(item)

    videoID = item["id"]["videoId"]

    videoURL = f"https://youtu.be/{videoID}?t=30"
    return videoURL


print("Le lien vers votre vidéo est :", getMusicInfos("lofi"))
