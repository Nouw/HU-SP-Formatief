from exporter.settings import createConnectionMongoDB
database = createConnectionMongoDB()

table = database.products

print(table)