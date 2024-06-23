#!/usr/bin/python3

"""
    A script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name_query = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database_name)

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE '{}' \
            ORDER BY id ASC".format(state_name_query))

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
