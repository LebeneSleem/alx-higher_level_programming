#!/usr/bin/python3
"""
This script lists all State objects and their corresponding City objects from the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database_name))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_and_cities = session.query(State, State.cities).order_by(State.id, State.cities.id).all()

    for state, city in states_and_cities:
        print("{}: {} ({})".format(state.name, city.id, city.name))

    session.close()
