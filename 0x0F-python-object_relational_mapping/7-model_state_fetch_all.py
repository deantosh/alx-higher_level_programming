#!/usr/bin/python3
"""
Script  lists all State objects from the database `hbtn_0e_6_usa`
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def create_db_engine(username, password, database):
    """
    Creates database engine
    """
    conn_string = "mysql://{}:{}@{}:{}/{}".format(
        username, password, 'localhost', 3306, database)

    # create engine
    engine = create_engine(conn_string)

    # return engine
    return engine


if __name__ == '__main__':
    # Extract command line arguments
    username, password, database = argv[1:]

    # Create engine
    engine = create_db_engine(username, password, database)

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
