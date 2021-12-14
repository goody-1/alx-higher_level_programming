#!/usr/bin/python3
"""
A "print_square" module.
The module prints a square with the character '#'
"""


def print_square(size):
    """
    The print square function
    print function -
    """
    # validating size attribute
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        pass
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
