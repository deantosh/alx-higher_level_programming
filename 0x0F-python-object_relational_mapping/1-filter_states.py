#!/usr/bin/python3
"""
Script lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa:
Requirements:
 - Your script should take 3 arguments: mysql username, mysql password
   and database name (no argument validation needed)
 - You must use the module MySQLdb (import MySQLdb)
 - Your script should connect to a MySQL server running on localhost
   at port 3306
 - Results must be sorted in ascending order by states.id
 - Results must be displayed as they are in the example below
 - Your code should not be executed when imported
"""
import sys
import MySQLdb

if __name__ == '__main__':
    """
    Connect to the database, get all states with name starting with 'N'
    """
    # connect to the database
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # create a cursor object to execute queries
    cursor = conn.cursor()

    # execute the query
    query = f"""
             SELECT *
             FROM states
             WHERE states.name
             LIKE 'N%'
             ORDER BY states.id ASC
             """
    cursor.execute(query)

    # fetch results
    results = cursor.fetchall()

    # print results
    for row in results:
        print(row)

    # close connection
    cursor.close()
    conn.close()
