from settings.database import createConnection

database = createConnection().huwebshop

table = database.sessions

for x in table.find():
    print(x)