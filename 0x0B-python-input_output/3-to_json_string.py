#!/usr/bin/python3
"""
Contains function that returns the JSON representation of a string object
"""
import json


def to_json_string(my_obj):
    """
    Args:
        my_obj -> string object to be represented

    Return:
        the JSON representation of the string object
    """

    return json.dumps(my_obj)
