from pymongo import MongoClient
from dotenv import load_dotenv
import os


def createConnection():
    load_dotenv()
    if os.getenv("DB_USE_AUTH") == 'True':
        return MongoClient("mongodb://$[username]:$[password]@$[hostlist]/$[huwebs]?authSource=$[authSource]")
    else:
        return MongoClient('localhost', 27017)

