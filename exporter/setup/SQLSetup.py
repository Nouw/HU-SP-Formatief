from settings.database import createConnectionMysqlDB

mycursor = createConnectionMysqlDB().cursor()

# delete database if database exists
mycursor.execute("DROP DATABASE IF EXISTS huwebshop")
# Create database
mycursor.execute("CREATE DATABASE huwebshop")
