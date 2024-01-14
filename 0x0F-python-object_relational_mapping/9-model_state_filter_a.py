#!/usr/bin/python3
"""
Script lists all State objects that contain the letter a
from the database `hbtn_0e_6_usa`
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def create_db_engine(username, password, database):
    """Creates and returns database engine"""
    # creata connection string
    conn_string = "mysql://{}:{}@{}:{}/{}".format(
        username, password, 'localhost', 3306, database
    )

    # create engine
    engine = create_engine(conn_string)

    # return engine
    return engine


if __name__ == '__main__':
    # Create variabes to pass to func
    username, password, database = argv[1:]

    # Create engine
    engine = create_db_engine(username, password, database)

    # Bind engine to base class
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query first state object
    states = session.query(State).filter(State.name.ilike('%a%')).all()

    # Print first state
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
