from sqlalchemy import Column, Boolean, ForeignKey, Integer, func, String
from sqlalchemy.ext.declarative import declarative_base
from exporter.migrations.create_producten_table import Products
from exporter.migrations.create_profiles_table import Profiles

Base = declarative_base()


class RecommendedBefore(Base):
    __tablename__ = "recommended_before"
    id = Column(Integer(), primary_key=True)
    product_id = Column(String(255), ForeignKey(Products.id))
    profile_id = Column(String(255), ForeignKey(Profiles.id))

    def __repr__(self):
        return 'id: {}'.format(self.id)
