import datetime
import sqlalchemy
from sqlalchemy import orm

from scripts.db_session import SqlAlchemyBase


class Item(SqlAlchemyBase):
    __tablename__ = 'items'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, unique=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    cost = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Float, default=cost * 1.2)
    weight = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    size = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    valuation = sqlalchemy.Column(sqlalchemy.Float, default=0.0)
    in_stock = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)

