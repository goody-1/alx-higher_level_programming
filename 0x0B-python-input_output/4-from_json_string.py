#!/usr/bin/python3
"""
Contains function that returns the JSON representation of a string object
"""
import json


def from_json_string(my_str):
    """
    Args:
        my_str -> json object to be returned as python data structure

    Return:
        python data structure represented by a JSON string
    """

    return json.loads(my_str)
