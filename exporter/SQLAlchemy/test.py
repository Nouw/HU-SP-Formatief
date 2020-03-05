import sqlalchemy
from .SQLAlchemy.producten_table import Product

engine = sqlalchemy.create_engine("mysql+pymysql://root:@localhost/huwebshop")

