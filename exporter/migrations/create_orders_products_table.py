from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from exporter.migrations.create_orders_table import Orders
from exporter.migrations.create_producten_table import Products

Base = declarative_base()


class OrdersProducts(Base):
    __tablename__ = "orders_products"
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer, ForeignKey(Orders.id))
    product_Id = Column(Integer, ForeignKey(Products.id_pk))
    amount = Column(Integer)

    def __repr__(self):
        return 'id: {}'.format(self.id)
