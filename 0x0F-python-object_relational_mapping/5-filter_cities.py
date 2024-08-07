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
    # variable to pass to query
    state_name = argv[4]
    # Execute query
    query = """
        SELECT cities.name
        FROM cities
        JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))
    # Fetch results
    result = cursor.fetchall()
    # variabes to format results
    str = ""
    my_list = []
    # create list from list of tuples
    for row in result:
        my_list.append(row[0])
    # create the string from list
    str = ', '.join(my_list)
    # print string
    print(str)
