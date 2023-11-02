#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database_name,
            port=3306
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Define the SQL query to retrieve cities and sort them by cities.id
        sql_query = "SELECT * FROM cities ORDER BY cities.id"

        # Execute the query
        cursor.execute(sql_query)

        # Fetch and print the results
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Close the cursor and the connection
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("Error:", e)
