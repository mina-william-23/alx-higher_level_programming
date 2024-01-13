#!/usr/bin/python3
"""
script that creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa
 """
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
import sys


def fetch_all():
    """Fetchs all states"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_to_add = 'California'
    city_to_add = 'San Francisco'

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # state has one to many relation with city
    # state can have many cities
    # so it will be more easy it create city first and save that state to it
    session.add(City(name=city_to_add, state=State(name=state_to_add)))
    session.commit()
    session.close()


if __name__ == "__main__":
    fetch_all()
