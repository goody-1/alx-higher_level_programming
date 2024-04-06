#!/usr/bin/python3

"""Adds two integers"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a (int, float): first number
        b (int, float): second number

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b is not an int or a float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    try:
        return int(a) + int(b)
    except Exception as e:
        raise (e)
