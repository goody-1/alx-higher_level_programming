#!/usr/bin/python3
"""Contains the is_same_class function"""


def is_same_class(obj, a_class):
    """
    Determines if an object is an instance of a given class

    Parameters:
        obj (object): The object to check
        a_class (type): The class to check against

    Returns:
        bool: True if obj is an instance of a_class, False otherwise
    """
    return type(obj) == a_class
