#!/usr/bin/python3
"""
script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
 """
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
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
    states = session.query(State).filter
    (State.name.like("%a%")).order_by
    (State.id).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    fetch_all()