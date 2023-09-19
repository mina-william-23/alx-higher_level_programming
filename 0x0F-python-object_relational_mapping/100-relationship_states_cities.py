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

    # one way to use cities list in states table
    # new_state = State(name='California')
    # new_state.cities.append(City(name='San Francisco'))
    # session.add(new_state)

    # another way to use city backref attribute state
    # which is set in relationship in State class
    # session.add(City(name="San Francisco", state=State(name="California")))

    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)
    session.add(new_state)
    session.add(new_city)
    session.commit()
    session.close()
