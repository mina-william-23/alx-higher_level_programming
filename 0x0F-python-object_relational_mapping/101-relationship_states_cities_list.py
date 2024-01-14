#!/usr/bin/python3
"""script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
 """


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
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('    {}: {}'.format(city.id, city.name))

    session.close()


if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from relationship_state import Base, State
    from relationship_city import City
    import sys
    fetch_all()
