#!/usr/bin/python3

"""
    A script that lists all states from the database hbtn_0e_0_usa
    Username, password and database names are given as user arguments.
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

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
