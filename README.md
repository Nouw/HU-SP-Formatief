# HU-SP-Formatiefw
Om alles goed op te zetten run de `exporter/setup/setup.sh`

# Installatie
Run `exporter/setup/setup.sh`

Voeg je database login etc to aan `exporter/.env`

 Vul daarna sqlalchemy.url in: `exporter/alembic.ini`
 
 voorbeeld van een sqlalchemy.url: `driver://user:pass@localhost/dbname`

Ga daarna naar `exporter/` en doe de volgende commands:

Deze command zorgt ervoor dat de kollomen worden gemaakt

`alembic revision -m "Start script"`

Deze command zorgt ervoor dat de veranderingen worden gepusht naar de database

`alembic upgrade head`

Daarna is je database klaar


# Vragen aan Nick
Hoe kan ik env variables gebruiken in .ini bestanden?

## Notes
Misschien hier even naar kijken om de data van MongoDB naar MySQL te zetten: https://docs.sqlalchemy.org/en/13/orm/tutorial.html

##Hoe werkt alembic?
Maak een baseline document aan met alle tabellen die je wilt toevoegen aan het begin.
Daarna kan je models maken in `exporter/migrations/`