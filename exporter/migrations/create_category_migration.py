from dotenv import load_dotenv
import os

from exporter.settings import createConnectionMongoDB, createConnectionMysqlDB

# Mysql variable to execute sql statements
myconnection = createConnectionMysqlDB()
mydbcur = myconnection.cursor()
mongocursor = createConnectionMongoDB()

mydbcur.execute("SHOW TABLES")

tables = []
for item in mydbcur.fetchall():
    tables.append(item[0].decode())

if 'categories' not in tables:
    # mydbcur.execute("CREATE TABLE categories (id int NOT NULL AUTO_INCREMENT, name CHAR NOT NULL)")
    mydbcur.execute("CREATE TABLE " + os.getenv("SQLDB_DATABASE") + ".categories ("
                    "id INT auto_increment NOT NULL,"
                    "name TEXT NULL,"
                    "PRIMARY KEY (id))")


mydbcur.execute("SELECT name FROM " + os.getenv("SQLDB_DATABASE") + ".categories")

categoryNames = []
for item in mydbcur.fetchall():
    categoryNames.append(item)

print(categoryNames)

# Get all the items from products
for item in mongocursor.products.find({"category": {"$ne": "null"}}).distinct("category"):
    if item not in categoryNames and item is not None:
        print(item)
        sql = "INSERT INTO " + os.getenv("SQLDB_DATABASE") + ".categories (name) VALUES (%s)"
        insertTuple = (item,)
        mydbcur.execute(sql, insertTuple)
        myconnection.commit()
    else:
        continue
