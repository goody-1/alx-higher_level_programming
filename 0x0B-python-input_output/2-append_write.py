#!/usr/bin/python3
"""
contains function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Args:
        filename -> name of file to be written
        text -> text to be written to the file

    Return:
        number of characters added
    """

    with open(filename, 'a', encoding="utf-8") as my_file:
        return my_file.write(text)
