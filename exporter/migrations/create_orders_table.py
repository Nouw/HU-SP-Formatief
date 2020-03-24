from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from exporter.migrations.create_sessions_table import Sessions
from exporter.migrations.create_producten_table import Products

Base = declarative_base()


class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer(), primary_key=True)
    session_id = Column(String(255), ForeignKey(Sessions.id))
    product_id = Column(String(255), ForeignKey(Products.id))

    def __repr__(self):
        return 'id: {}'.format(self.id)
