from sqlalchemy import Column, Boolean, ForeignKey, Integer, func, DateTime
from sqlalchemy.ext.declarative import declarative_base
from exporter.migrations.create_producten_table import Products
from exporter.migrations.create_profiles_table import Profiles

Base = declarative_base()


class RecommendedBefore(Base):
    __tablename__ = "recommended_before"
    id = Column(Integer(), primary_key=True)
    product_id = Column(Integer, ForeignKey(Products.id_pk))
    profile_id = Column(Integer, ForeignKey(Profiles.id_pk))

    def __repr__(self):
        return 'id: {}'.format(self.id)
