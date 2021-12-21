#!/usr/bin/python3
"""Module contains function that checks if object is a subclass of
the specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class inherited
    (directly or indirectly from the specified class;
    False otherwise)
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
