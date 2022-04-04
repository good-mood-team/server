import requests as req
import random

API_KEY = "AIzaSyAfHh4ljEXd3de6i5Daw5xG6mtlJYGkThE"
BASE_URL = "https://youtube.googleapis.com/youtube/v3"


def getMusicInfos(genre) -> str:
    r = req.get(f"{BASE_URL}/search?maxResults=2&q={genre}%20instrumental&type=video&key={API_KEY}")
    r = r.json()

    rnd = random.randint(0, len(r["items"]) - 1)
    item = r["items"][rnd]

    videoId = item["id"]["videoId"]

    return videoId
