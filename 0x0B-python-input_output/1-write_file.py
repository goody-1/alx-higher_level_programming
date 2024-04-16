#!/usr/bin/python3
"""
contains function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Args:
        filename -> name of file to be written
        text -> text to be written to the file

    Return:
        number of characters written
    """

    with open(filename, 'w', encoding="utf-8") as my_file:
        return my_file.write(text)
