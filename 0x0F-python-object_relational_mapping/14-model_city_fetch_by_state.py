#!/usr/bin/python3
"""
script that prints all City objects from the database hbtn_0e_14_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
import sys


def fetch_all():
    """Fetchs all"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()
    for state, city in data:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()


if __name__ == "__main__":
    fetch_all()
