#!/usr/bin/python3
"""
Contains function append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Args:
        filename -> name of file
        search_string -> string text is to be appended after
        new_string -> new string to append

    """

    new_text = ""

    with open(filename, 'r+') as file:
        for line in file:
            new_text += line
            if search_string in line:
                new_text += new_string

    with open(filename, mode="w") as file:
        file.write(new_text)
