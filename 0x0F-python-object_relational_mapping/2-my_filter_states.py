#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
Requirements:
 - Your script should take 4 arguments: mysql username, mysql password,
   database name and state name searched (no argument validation needed)
 - You must use the module MySQLdb (import MySQLdb)
 - Your script should connect to a MySQL server running on localhost at
   port 3306
 - You must use format to create the SQL query with the user input
 - Results must be sorted in ascending order by states.id
 - Results must be displayed as they are in the example below
 - Your code should not be executed when imported
"""
import sys
import MySQLdb


if __name__ == '__main__':
    """
    Connects to the database, displays all values in the states table
    where name matches argument.
    """

    # retrieve state name
    state_name = sys.argv[4]

    # connect to the database
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # create cursor object - execute queries
    cursor = conn.cursor()

    # execute sql query
    query = f"""
             SELECT *
             FROM states
             WHERE BINARY states.name
             LIKE '{state_name}%'
             ORDER BY states.id ASC
             """
    cursor.execute(query)

    # fetch results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # close connections
    cursor.close()
    conn.close()
