import requests as req
import random

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


def getMusicLyrics(id):
    pass
    return lyrics


def findChorus(lyrics):
    pass
    return chorusTimeCode


def getMusicUrl(name, chorusTimeCode):
    pass
    return url
