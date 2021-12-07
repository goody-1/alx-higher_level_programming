#!/usr/bin/python3

"""This module contains a class - Square
This is based on "5-square" but now prints the square
"""


class Square():
    """Square class with private attribute - size
    size must be an integer, TypeError and ValueError exceptions are raised
    when they occur

    methods:
        set_size - sets the size of the square
        get_size - gets the size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize object
        Instantiation with integer size which is optional
        """
        # validating size instance attribute
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        # validating position instance attribute
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for item in position:
            try:
                if type(item) != int or item < 0:
                    raise TypeError("position must be a tuple of 2"
                                    "positive integers")
            except Exception:
                raise TypeError("position must be a tuple of 2"
                                "positive integers")

        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    def area(self):
        """This returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """This function prints the square
        """
        if self.__size == 0:
            print()
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()

        __space_no = self.__position[0] * " "
        for i in range(self.__size):
            print("{}".format(__space_no), end="")
            for j in range(self.__size):
                print("#", end="")
            print()
