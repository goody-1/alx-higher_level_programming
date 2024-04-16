#!/usr/bin/python3
"""
contains function that reads utf-8 file
"""


def read_file(filename=""):
    """Read file"""

    with open(filename, 'r', encoding="utf-8") as my_file:
        print(my_file.read(), end="")
