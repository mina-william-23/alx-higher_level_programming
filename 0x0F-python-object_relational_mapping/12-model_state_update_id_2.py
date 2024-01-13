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
    state_id_edit = 2
    state_new_name = 'New Mexico'

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).\
    filter_by(id=state_id_edit).update({State.name: state_new_name})
    session.commit()
    session.close()


if __name__ == "__main__":
    fetch_all()
