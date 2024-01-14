#!/usr/bin/python3
"""
Script prints the first State object from the database `hbtn_0e_6_usa`
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def create_db_engine(username, password, database):
    """Creates and returns database engine"""
    # creatae connection string
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
    first_state = session.query(State).first()

    # Print first state
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))

    # Close the session
    session.close()
