#!/usr/bin/python3
import sys
import MySQLdb

if len(sys.argv) == 4:
    # db config credentials
    db_config = {
        'host': 'localhost',
        'user': sys.argv[1],
        'password': sys.argv[2],
        'database': sys.argv[3],
        'port': 3306
    }

    # Create database connection
    with MySQLdb.connect(**db_config) as conn:
        # cursor obect to connect to database
        with conn.cursor() as cursor:
            # Execute SQL queries
            query = "SELECT * FROM states ORDER BY states.id"
            cursor.execute(query)

            # Fetch and print result
            results = cursor.fetchall()
            for row in results:
                print(row)
