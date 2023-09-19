#!/usr/bin/python3
''' model state module '''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City

# this Base will cause error so always use one Base class
# and import it everywhere
# Base = declarative_base()
# iam keeping this to remember that error


class State(Base):
    '''Represents a state for a MySQL database.

    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    cities (sqlalchemy.orm.relationship): The State-City relationship.'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
