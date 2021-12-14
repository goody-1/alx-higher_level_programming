#!/usr/bin/python3
"""
The "say_my_name" Module.
This module contains a function that prints
"My name is <first name> <last name>

For example,

>>> say_my_name("Luke", "Freeman")
My name is Luke Freeman
"""


def say_my_name(first_name, last_name=""):
    """
    Returns a string - My name is <first name> <last name>
    Args:
        first_name - a string
        last_name - also a string
    """

    # validate the parameters
    if first_name is None:
        raise TypeError("first_name must be a string")
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")

    try:
        return "My name is {} {}".format(first_name, last_name)
    except TypeError:
        raise TypeError("first_name must be a string")
