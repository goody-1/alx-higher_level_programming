#!/usr/bin/python3

"""
    A script that takes in the name of a state as an argument
    and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database_name)

    cursor = db.cursor()

    cursor.execute(
        """SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE %s
        ORDER BY cities.id ASC
        """, (state,))

    query_rows = cursor.fetchall()

    if query_rows:
        string_rows = [row[0] for row in query_rows]

        for row in string_rows:
            if row != string_rows[-1]:
                print(row, end=', ')
            else:
                print(row)
    else:
        print()

    cursor.close()
    db.close()
