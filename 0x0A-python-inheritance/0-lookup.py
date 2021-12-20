#!/usr/bin/python3
"""
A lookup module, contains a function that returns a
list of available attributes and methods of an object

Function:
    lookup -> def lookup(obj)
"""


def lookup(obj):
    """
    Return:
        a list object

    Parameter:
        obj -> object whose attributes and methods are to be returned
    """

    return [key for key in obj.__dict__]
