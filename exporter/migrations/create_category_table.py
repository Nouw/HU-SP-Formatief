from sqlalchemy import create_engine, MetaData, inspect, Column, Integer, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
db_uri = 'mysql+pymysql://root:@localhost/huwebshop'
engine = create_engine(db_uri)

meta = MetaData(engine)

Base = declarative_base()


class CategoryTemplateTable(object):
    id = Column(Integer, primary_key=True)
    name = Column(Text)


class CategoryTable(CategoryTemplateTable, Base):
    __tablename__ = 'category'


def createTableCategory():
    Base.metadata.create_all(bind=engine)
