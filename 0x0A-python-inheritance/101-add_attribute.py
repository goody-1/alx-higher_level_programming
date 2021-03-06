#!/usr/bin/python3
"""
Contains function add_attribute that add new attribute to an object if possible
"""


def add_attribute(obj, name, value):
    """ class MyInt that inherits from int

    Arguments:
        obj (obj) -- object
        name (str) -- name
        value (*) -- value
    Raises:
        TypeError: can't add new attribute.
    """
    if hasattr(obj, "__dict__"):
        obj.__setattr__(name, value)
    else:
        raise TypeError("can't add new attribute")
