from pymongo import MongoClient
import mysql.connector

from dotenv import load_dotenv
import os


def createConnectionMongoDB():
    load_dotenv()
    if os.getenv("DB_USE_AUTH") == 'True':
        return MongoClient("mongodb://$[username]:$[password]@$[hostlist]/$[huwebs]?authSource=$[authSource]")
    else:
        return MongoClient(host=os.getenv("MONGODB_HOST"), port=int(os.getenv("MONGODB_PORT")))[os.getenv("MONGODB_DATABASE")]


def createConnectionMysqlDB():
    from dotenv import load_dotenv
    import os

    load_dotenv()
    if os.getenv("SQLDB_USE_AUTH") == 'True':
        return mysql.connector.connect(
            host=os.getenv("SQLDB_HOST"),
            user=os.getenv("SQLDB_USERNAME"),
            passwd=os.getenv("SQLDB_PASSWORD"),
            database=os.getenv("SQLDB_DATABASE")
        )
    else:
        return mysql.connector.connect(
            host=os.getenv("SQLDB_HOST"),
        )

