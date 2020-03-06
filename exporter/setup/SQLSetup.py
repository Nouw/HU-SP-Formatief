# # from settings.database import createConnectionMysqlDB
# # from ..settings.database import createConnectionMysql
# from ..settings
# mycursor = createConnectionMysqlDB().cursor()
#
# # delete database if database exists
# mycursor.execute("DROP DATABASE IF EXISTS huwebshop")
# # Create database
# mycursor.execute("CREATE DATABASE huwebshop")

# from exporter.settings.database import createConnectionMysqlDB
import exporter.settings.database as mysql

engine = mysql.createConnectionMysqlDB().connect()

engine.execute("CREATE DATABASE test")
engine.close()

# print(mysql.createConnectionMysqlDB())
import time


# engine = createConnectionMysqlDB


# print(createConnectionMysqlDB)

# con = createConnectionMysqlDB
# time.sleep(.20)
# # print(con)
# mycursor = con.cursor()

# # Delete database if exists
# mycursor.execute("DROP DATABASE IF EXISTS huwebshop")
# # Create database
# mycursor.execute("CREATE DATABASE huwebshop")
