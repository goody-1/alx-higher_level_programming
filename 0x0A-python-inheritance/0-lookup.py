#!/usr/bin/python3
""" Contains `lookup` function """


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Parameters:
    obj (object): The object to inspect

    Returns:
    list: A list of strings representing the attributes and
            methods of the object
    """
    return dir(obj)
