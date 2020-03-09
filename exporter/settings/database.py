from pymongo import MongoClient
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os




def createConnectionMongoDB():
    load_dotenv()
    if os.getenv("DB_USE_AUTH") == 'True':
        return MongoClient("mongodb://$[username]:$[password]@$[hostlist]/$[huwebs]?authSource=$[authSource]")
    else:
        return MongoClient(host=os.getenv("MONGODB_HOST"), port=int(os.getenv("MONGODB_PORT")))[
            os.getenv("MONGODB_DATABASE")]


def createConnectionMysqlDB():
    load_dotenv()

    if os.getenv("SQLDB_USE_AUTHB") == 'True':
        db_uri = 'mysql+pymysql://' + os.getenv('SQLDB_USERNAME') + ':'+ os.getenv('SQLDB_PASSWORD') + '@' + os.getenv('SQLDB_HOST') + '/' + os.getenv('SQLDB_DATABASE')
        return create_engine(db_uri)
    else:
        db_uri = 'mysql+pymysql://' + os.getenv('SQLDB_USERNAME') + ':@' + os.getenv('SQLDB_HOST') + '/' + os.getenv('SQLDB_DATABASE')
        return create_engine(db_uri)
    # if os.getenv("SQLDB_USE_AUTH") == 'True':
    #     try:
    #         return mysql.connector.connect(
    #             host=os.getenv("SQLDB_HOST"),
    #             user=os.getenv("SQLDB_USERNAME"),
    #             passwd=os.getenv("SQLDB_PASSWORD"),
    #             database=os.getenv("SQLDB_DATABASE")
    #         )
    #     except:
    #         print('Cannot connect to database')
    #         return 0
    # else:
    #     try:
    #         return mysql.connector.connect(
    #             host=os.getenv("SQLDB_HOST"),
    #         )
    #     except:
    #         print('Cannot connect to database')
    #         return 0
