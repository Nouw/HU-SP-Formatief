from sqlalchemy import Column, Boolean, String, Integer, func, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Products(Base):
    __tablename__ = 'products'
    id_pk = Column(Integer(), primary_key=True)
    name = Column(String(255))
    description = Column(Text)
    brand = Column(String(255))
    price = Column(Integer())
    discount = Column(Integer())
    stock = Column(Integer())
    category = Column(String(255))
    sub_category = Column(String(255))
    sub_sub_category = Column(String(255))
    sub_sub_sub_category = Column(String(255))
    recommandable = Column(Boolean())
    online_only = Column(Boolean())
    target_demographic = Column(String(255))
    gender = Column(String(90))  # Change this to enum because only 3 genders (Man, Vrouw, Overig)
    color = Column(String(100))  # Also change this to an enum because there are only 20 ish colors
    unit = Column(String(255))
    odor_type = Column(String(255))
    series = Column(String(255))
    kind = Column(String(255))
    variant = Column(String(255))
    type = Column(String(255))
    type_of_hair_care = Column(String(255))
    type_of_hair_coloring = Column(String(255))
    # test = relationship("RecommendedBefore", secondary=)

    def __repr__(self):
        return 'id: {}'.format(self.id_pk)