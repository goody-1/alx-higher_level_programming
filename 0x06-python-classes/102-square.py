#!/usr/bin/python3

"""This module contains a class - Square
This is based on "4-square" but now makes the instances comparable
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

    @property
    def size(self):
        """Get square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set square size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """This returns the current square area
        """
        return self.size ** 2

    def __str__(self):
        """String representation of Square class"""
        return "{}".format(self.area())

    def __eq__(self, other):
        """Comparable class - check if equal"""
        return self.area() == other.area()

    def __lt__(self, other):
        """Comparable class - check if self is less than other"""
        return self.area() < other.area()

    def __le__(self, other):
        """Comparable class - check if self is less than or equal to other"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Comparable class - check if self is greater than other"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Comparable class - check if self is greater than or equal to other
        """
        return self.area() >= other.area()

    def __ne__(self, other):
        """Comparable class - check if self is not equal to other"""
        return self.area() != other.area()
