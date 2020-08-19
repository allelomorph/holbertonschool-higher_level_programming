#!/usr/bin/python3
"""0x0F. Python - Object-relational mapping - task 15. City relationship
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Defines ORM class for table `states`, with 2 columns:

       `id` (Column): unique identifier, primary key
       `name` (Column): name of state
       `cities` (relationship): one-to-many-association to `City`
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state")
