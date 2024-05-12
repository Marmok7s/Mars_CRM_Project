import datetime
import sqlalchemy
from sqlalchemy import orm

from scripts.db_session import SqlAlchemyBase
import scripts.models.client as clients


class Order(SqlAlchemyBase):
    __tablename__ = 'orders'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    client = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('clients.id'))
    items_list = sqlalchemy.Column(sqlalchemy.String)
    delivery = sqlalchemy.Column(sqlalchemy.String, nullable=True, default=None)
    is_paid = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    payment_method = sqlalchemy.Column(sqlalchemy.String, default='debit_card')
    total_price = sqlalchemy.Column(sqlalchemy.Float)

    customer = orm.relationship(clients.Client)
