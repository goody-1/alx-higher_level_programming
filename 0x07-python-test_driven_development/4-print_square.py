#!/usr/bin/python3

"""Prints a square with the character #"""


def print_square(size):
    """
    Prints a square of a given size using the '#' character.

    Args:
        size (int): The size of the square.

    Returns:
        None
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        print("#" * size)
