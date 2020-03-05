from sqlalchemy import create_engine, MetaData, Column, Integer, Text, Boolean, ForeignKey, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .create_category_table import CategoryTable

db_uri = 'mysql+pymysql://root:@localhost/huwebshop'
engine = create_engine(db_uri)

meta = MetaData(engine)

Base = declarative_base()


class ProductenTemplateTable(object):
    id_pk = Column(Integer, primary_key=True)
    _id = Column(Text)
    brand = Column(Text)
    # category = Column(Integer, ForeignKey('category.name'))
    description = Column(Text),
    gender = Column(Text),
    name = Column(Text)
    recommandable = Column(Boolean)
    sub_category = Column(Text)
    sub_sub_category = Column(Text)
    sub_sub_sub_category = Column(Text)


class ProductenTable(ProductenTemplateTable, Base):
    __tablename__ = 'producten'


def createTableProducten():
    # Base.metadata.create_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    ins = inspect(engine)
    for _t in ins.get_table_names():
        print(_t)

    # ins = inspect(engine)
    # for _t in ins.get_table_names():
    #     print(_t)