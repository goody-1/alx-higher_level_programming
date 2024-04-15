#!/usr/bin/python3
"""Contains the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    Determines if an object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class

    Parameters:
        obj (object): The object to check
        a_class (type): The class to check against

    Returns:
        bool: True if obj is an instance of a class that inherited
                from a_class,
        False otherwise
    """
    return isinstance(obj, a_class)
