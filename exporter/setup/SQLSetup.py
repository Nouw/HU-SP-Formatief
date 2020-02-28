import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
if os.getenv("SQLDB_USE_AUTH") == 'True':
    mydb = mysql.connector.connect(
        host=os.getenv("SQLDB_HOST"),
        user=os.getenv("SQLDB_USERNAME"),
        passwd=os.getenv("SQLDB_PASSWORD")
    )
else:
    mydb = mysql.connector.connect(
        host=os.getenv("SQLDB_HOST"),
    )

mycursor = mydb.cursor()

# delete database if database exists
mycursor.execute("DROP DATABASE IF EXISTS huwebshop")
# Create database
mycursor.execute("CREATE DATABASE huwebshop")
