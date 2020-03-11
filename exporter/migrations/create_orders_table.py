from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from exporter.migrations.create_sessions_table import Sessions

Base = declarative_base()


class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer(), primary_key=True)
    session_id = Column(Integer, ForeignKey(Sessions.id_pk))

    def __repr__(self):
        return 'id: {}'.format(self.id)
