#!/usr/bin/python3
"""
Contains function that write a n Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj -> python object to be represented by JSON
        filename -> name of file to write to

    Return:
        python data structure represented by a JSON string
    """

    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
