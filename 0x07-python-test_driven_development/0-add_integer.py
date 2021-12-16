#!/usr/bin/python3
"""
The "Add Integers" Module.
This module adds just two integers via the function, add_integer().
For example,

>>> add_integer(34, 8)
42
"""


def add_integer(a, b=98):
    """
    Return the sum of the two integers 'a' and 'b', an exact integer.

    Example:

    >>> add_integer(10)
    108

    >>> add_integer(-76, -4)
    -80

    """

    # Checking if "NaN" is one of the inputs
    if a is float('NaN') or b is float('NaN'):
        raise ValueError("cannot convert float NaN to integer")

    # Validating the types of inputs
    # input must be integer or float (which will be converted)
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    #   converting floats to integers
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89

    return result
