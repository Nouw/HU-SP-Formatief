from exporter.migrations.create_producten_table import Producten


def __init__(self):
    self.createProducten = Producten.__table__


def __del__(self):
    self.con.close()
