#!/usr/bin/python3
"""0x0F. Python - Object-relational mapping - task 6. First state model
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Defines ORM class for table `states`, with 2 columns:

       `id` (sqlalchemy.Column): unique identifier, primary key
       `name` (sqlalchemy.Column): name of state

    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
