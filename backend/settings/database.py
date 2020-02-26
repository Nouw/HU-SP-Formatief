from pymongo import MongoClient
from dotenv import load_dotenv
import os


def createConnection():
    load_dotenv()
    if os.getenv("DB_USE_AUTH") == 'True':
        return MongoClient("mongodb://$[username]:$[password]@$[hostlist]/$[huwebs]?authSource=$[authSource]")
    else:
        return MongoClient(host=os.getenv("MONGODB_HOST"), port=int(os.getenv("MONGODB_PORT")))[os.getenv("MONGODB_DATABASE")]

