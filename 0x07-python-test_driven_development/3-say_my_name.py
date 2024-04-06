#!/usr/bin/python3
"""Prints a name"""


def say_my_name(first_name, last_name=""):
    """Prints a name

    Args:
        first_name (str): first name
        last_name (str): last name

    Raises:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
