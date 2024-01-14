#!/usr/bin/python3
"""
State module
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


# Define a Model
Base = declarative_base()


# define state table
class State(Base):
    """Represents a state for a MySQL database.

    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                unique=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City',
                          back_populates='states',
                          cascade='all, delete')
