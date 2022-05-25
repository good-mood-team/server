import requests as req
import random


BASE_URL = "https://youtube.googleapis.com/youtube/v3"

MAX_RESULTS = 2


def getMusicInfos(genre, API_KEY) -> str:
    r = req.get(f"{BASE_URL}/search?maxResults={MAX_RESULTS}&q={genre}%20instrumental%201h&type=video&key={API_KEY}")
    r = r.json()

    rnd = random.randint(0, len(r["items"]) - 1)
    item = r["items"][rnd]

    videoId = item["id"]["videoId"]

    return videoId
