#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa for a specific state.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 5:
        usage_message = (
            "Usage: {} <username> <password> <database_name> <state_name>"
        ).format(sys.argv[0])
        print(usage_message)
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

        # Define the SQL query to retrieve cities of the specified state
        sql_query = (
            "SELECT cities.id, cities.name, states.name FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s ORDER BY cities.id"
        )

        # Execute the query with the state_name parameter
        cursor.execute(sql_query, (state_name,))

        # Fetch and print the results
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Close the cursor and the connection
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("Error:", e)
