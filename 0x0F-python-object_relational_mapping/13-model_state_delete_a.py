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
    # synchronize session = false , don't reflect changes on actual database
    # i will reflect that with commit()
    session.query(State).\
        filter(State.name.like("%a%")).\
        delete(synchronize_session=False)
    session.commit()
    session.close()


if __name__ == "__main__":
    fetch_all()
