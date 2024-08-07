#!/usr/bin/python3
"""
Script prints a city objects from the database `hbtn_0e_14_usa`
"""

from sys import argv
from model_state import State
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_db_engine(username, password, database):
    """create and returns db engine"""
    # conn string
    conn_string = "mysql://{}:{}@{}:{}/{}".format(
        username, password, 'localhost', 3306, database)

    # Create db engine
    engine = create_engine(conn_string)

    # Return engine
    return engine


if __name__ == '__main__':
    # Extract command line arguments
    username, password, database = argv[1:]

    # Create db engine
    engine = create_db_engine(username, password, database)

    # Bind engine to base class
    Base.metadata.bind = engine

    # Create session to connect to db
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query city table
    cities = session.query(City).all()

    # Print results
    for city in cities:
        # Get the state of each city
        state = session.query(State).filter_by(id=city.state_id).first()
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()
