#!/usr/bin/python3

"""This module contains a class - Square
This is based on "4-square" but now prints the square
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
        return self.__size ** 2

    def my_print(self):
        """This function prints the square
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
