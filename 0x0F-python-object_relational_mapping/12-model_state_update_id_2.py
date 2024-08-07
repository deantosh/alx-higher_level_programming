#!/usr/bin/python3
"""
Script updates State objects where id = 2
in the database `hbtn_0e_6_usa`
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

    # Get the obect to update
    update_state = session.query(State).filter_by(id=2).first()

    # Update the object
    update_state.name = "New Mexico"

    # Commit changes to database
    session.commit()

    # Close the session
    session.close()
