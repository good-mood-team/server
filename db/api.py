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


def add_results(db, payload) -> int:
    """
    Adds a results to the database
    :param db: The database instance.
    :param payload: The informations about the user (age, gender) + results.
    """
    ts = datetime.datetime.now().timestamp()

    try:
        if payload["age"] and payload["gender"] and payload["results"]:
            if int(payload["gender"]) == 1:
                gender = "MALE"

            elif int(payload["gender"]) == 2:
                gender = "FEMALE"

            elif int(payload["gender"]) == 3:
                gender = "OTHER"

            for genre in payload["results"]:
                db.users.insert_one(
                    {
                        "age": payload["age"],
                        "gender": gender,
                        "genre": genre,
                        "results": payload["results"][genre],
                        "created_at": ts,
                    }
                )

        else:
            return {"status": 400, "message": "A value in the payload is null."}

        return {"status": 200, "message": "Successfully added results to the database."}

    except Exception:
        return {"status": 500, "message": "An error occured."}
