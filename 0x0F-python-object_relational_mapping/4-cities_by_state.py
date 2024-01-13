#!/usr/bin/python3
"""
This script all cities from the database hbtn_0e_4_usa
"""


from sys import argv
import MySQLdb

if __name__ == '__main__':
    # db config
    conn = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        password=argv[2],
        database=argv[3],
        port=3306
    )
    # db config object
    cursor = conn.cursor()
    # Execute query
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states
        ON cities.id = states.id
        ORDER BY cities.id
    """
    cursor.execute(query)
    # Fetch and print results
    results = cursor.fetchall()
    if results is not None:
        for row in results:
            print(row)
