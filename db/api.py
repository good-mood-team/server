import datetime
from pymongo import MongoClient


def connect(host="localhost", port=27017) -> dict:
    """
    Creates the connection to the database
    """
    try:
        conn = MongoClient(host, port)
        print("Connected successfully to MongoDB!")
        return conn
    except:
        raise Exception("Could not connect to MongoDB...")


def add_user(db, payload) -> int:
    """
    Adds a user to the database
    :param db: The database instance.
    :param payload: The informations about the user (age, gender) + results.
    """
    ts = datetime.datetime.now().timestamp()

    try:
        if payload["age"] and payload["gender"]:
            if payload["gender"] == 1:

                gender = "MALE"

            elif payload["gender"] == 2:

                gender = "FEMALE"

            elif payload["gender"] == 3:

                gender = "OTHER / UNSPECIFIED"

            for genre in payload["results"]:

                db.user.insert_one(
                    {"age": payload["age"], "gender": gender, "genre": genre, "results": payload["results"][genre], "created_at": ts})

        else:

            return {"status": 400, "message": "Payload should not be null."}

        return {"status": 200, "message": "Successfully added results to the database."}

    except Exception:
        return {"status": 500, "message": "An error occured."}
