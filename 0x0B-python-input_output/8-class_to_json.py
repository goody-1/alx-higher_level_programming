#!/usr/bin/python3
"""
Contains function that returns the dictionary description with simple data
structure for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Args:
        obj -> an instance of a class

    Return:
        dictionary description - json format
    """

    return obj.__dict__
