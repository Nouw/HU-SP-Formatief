from .database import createConnectionMongoDB
from .database import createConnectionMysqlDB


def __init__(self):
    self.con = createConnectionMysqlDB()


def __del__(self):
    self.con.close()
