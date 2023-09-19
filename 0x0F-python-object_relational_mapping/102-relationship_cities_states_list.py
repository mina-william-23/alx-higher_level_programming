#!/usr/bin/python3
''' model_state_fetch_all '''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    usr = argv[1]
    paswd = argv[2]
    dt = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        usr, paswd, dt, pool_pre_ping=True))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
