import requests as req
import random
<<<<<<< HEAD
=======

BASE_URL = "http://api.musixmatch.com/ws/1.1/"
API_KEY = "c82cd9b49b81240563733e813a4a0198"


def getEndpoint(method, args):
    return BASE_URL + method + "?format=json&callback=callback&" + args + "&apikey=" + API_KEY


def getMusicInfos(genre):
    rdnItem = random.randint(0, 100)
    endpoint = getEndpoint(
        "track.search", f"f_has_lyrics=1&f_music_genre_name={genre}&page_size=100&page=1&s_track_rating=asc"
    )
    r = req.get(endpoint)
    print(r.json()["message"]["body"]["track_list"][rdnItem])
    # return name, id
    # A FIX
    
    response = req.get("https://api.soundcloud.com/tracks?q=hello&ids=1,2,3&genres={genre}&access=playable&limit=3&linked_partitioning=true")


getMusicInfos("JAZZ")
>>>>>>> 5e7a754dfcea6dedb73979dbf3fa8c38ed4b84cc

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
