#!/usr/bin/python3
"""
script that lists all City objects from the database hbtn_0e_101_usa
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

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
    session.close()


if __name__ == "__main__":
    fetch_all()
