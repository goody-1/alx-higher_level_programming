#!/usr/bin/python3
"""
Contains function that checks that an object is exactly an instance of
the specified class
"""


def is_same_class(obj, a_class):
    """
    Returns:
        True -> if object is exactly an instance of the specified class
            else: False
    """
    return type(obj) == a_class
