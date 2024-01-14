#!/usr/bin/python3
"""
Script  lists all State objects from the database `hbtn_0e_6_usa`
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Create engine
    engine = create_engine('mysql://root:root@localhost:3306/hbtn_0e_6_usa')

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all state objects
    states = session.query(State).all()

    # Print states
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
