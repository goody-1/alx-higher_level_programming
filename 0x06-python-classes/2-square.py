#!/usr/bin/python3

"""This module contains a class - Square
"""


class Square():
    """Square class with private attribute - size
    size must be an integer, TypeError and ValueError exceptions are raised
    when they occur

    methods:
        set_size - sets the size of the square
        get_size - gets the size of the square
    """

    def __init__(self, size=0):
        """Initialize object
        Instantiation with integer size which is optional
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def set_size(self, size):
        """Set square size
        """
        self.__size = size

    def get_size(self):
        """Get square size
        """
        return self.__size
