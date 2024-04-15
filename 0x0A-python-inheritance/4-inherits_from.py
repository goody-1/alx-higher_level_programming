#!/usr/bin/python3
"""Contains the inherits_from function"""


def inherits_from(obj, a_class):
    """
    Determines  if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Parameters:
        obj (object): The object to check
        a_class (type): The class to check against

    Returns:
        bool: True if obj is an instance of a class that inherited from a_class,
        False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
