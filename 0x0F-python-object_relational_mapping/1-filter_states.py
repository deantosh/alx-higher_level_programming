#!/usr/bin/python3
"""
This script lists all states with a name starting with N
from the database hbtn_0e_0_usa.
"""


from sys import argv
import MySQLdb

if __name__ == '__main__':
    """
    Access to the db and get the states.
    """
    # Create database connection
    conn = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3],
        port=3306
    )
    # cursor obect to connect to database
    cursor = conn.cursor()
    # Execute SQL queries
    query = "SELECT * FROM states WHERE BINARY states.name LIKE 'N%'"
    cursor.execute(query)
    # Fetch results
    results = cursor.fetchall()
    # Print results
    for row in results:
        print(row)
