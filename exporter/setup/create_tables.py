import exporter.migrations as migration

print('Creating all tables')
migration.createTableProducten()
migration.createTableCategory()