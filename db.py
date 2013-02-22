#!/usr/bin/env python
# coding: utf8
from config import *

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import Session


from sqlalchemy import (create_engine, MetaData, Column, Integer, String)

from sqlalchemy import func


Base = declarative_base()


class Item(Base):

    __tablename__ = 'items'

    item_id = Column(Integer, primary_key=True, autoincrement=True)

    item_name = Column(String(30), nullable=False)


if __name__ == '__main__':

    engine = create_engine('sqlite:///:memory:', echo=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    # make some records
    session.query(Item).delete()

    session.add_all([

        Item(item_name='Item 1'),

        Item(item_name='Item 2'),

        Item(item_name='Item 3'),

        Item(item_name='Item 4')

    ])

    session.commit()

    print session.query(Item.item_name).all()
    # test random results
    for i in range(5):

        print session.query(Item.item_name).order_by(func.random()).all()
