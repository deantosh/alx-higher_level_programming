#!/usr/bin/python3
"""
This script lists a states from the
database hbtn_0e_0_usa.
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
    # Set the variabe in python
    state_name = argv[4]
    query = "SELECT * FROM states WHERE name LIKE %s"
    cursor.execute(query, (state_name,))
    # Fetch results
    results = cursor.fetchall()
    # Print results
    for row in results:
        print(row)
