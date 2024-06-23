#!/usr/bin/python3

"""
    A script that lists all cities from the database hbtn_0e_4_usa
    sorted in ascending order by cities.id.
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database_name)

    cursor = db.cursor()

    cursor.execute(
        """SELECT ROW_NUMBER() OVER (ORDER BY cities.id) AS row_id,
        cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """)

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
