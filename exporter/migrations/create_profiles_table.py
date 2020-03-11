from sqlalchemy import Column, Boolean, String, Integer, func, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# from exporter.migrations.create_buids_table import Buids

Base = declarative_base()


class Profiles(Base):
    __tablename__ = "profiles"
    id_pk = Column(Integer(), primary_key=True)
    id = Column(String(255))
    first_order = Column(DateTime)
    latest_order = Column(DateTime)
    order_amount = Column(Integer)

    # buid = relationship(Buids)

    def __repr__(self):
        return 'id: {}'.format(self.id_pk)
