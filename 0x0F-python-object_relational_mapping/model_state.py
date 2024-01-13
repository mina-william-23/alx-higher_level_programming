#!/usr/bin/python3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Define a Model
Base = declarative_base()


# define state table
class State(Base):
    '''state table'''
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                unique=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128),
                  nullable=False)
