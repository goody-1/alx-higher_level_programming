#!/usr/bin/python3

"""This module contains a class - Square
This is based on "6-square" but now prints the square
"""


class Square():
    """Square class with private attribute - size
    size must be an integer, TypeError and ValueError exceptions are raised
    when they occur

    methods:
        set_size - sets the size of the square
        get_size - gets the size of the square
        area - calculates the area of the square
        my_print - prints the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize object
        Instantiation with integer size which is optional
        """
        # validating size instance attribute
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        # validating position instance attribute
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        for item in position:
            try:
                if not isinstance(item, int) or item < 0:
                    raise TypeError("position must be a tuple of 2 "
                                    "positive integers")
            except Exception:
                raise TypeError("position must be a tuple of 2 "
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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Gets the position for the square to be printed
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position for the square to be printed
        """
        # validating position instance attribute
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for item in value:
            try:
                if not isinstance(item, int) or item < 0:
                    raise TypeError("position must be a tuple of 2 "
                                    "positive integers")
            except Exception:
                raise TypeError("position must be a tuple of 2 "
                                "positive integers")
        self.__position = value

    def area(self):
        """This returns the current square area
        """
        return self.size ** 2

    def my_print(self):
        """This function prints the square
        """
        if self.size == 0:
            print()
        elif self.position[1] > 0:
            for i in range(self.position[1]):
                print()

        __space_no = self.position[0] * " "
        for i in range(self.size):
            print("{}".format(__space_no), end="")
            for j in range(self.size):
                print("#", end="")
            print()

    def __str__(self):
        """String representation of Square instance

        Return:
            Formatted string representing the square
        """
        if self.size == 0:
            return ""

        string = ("\n" * self.position[1]) + (
            " " * self.position[0] + "#" * self.size + "\n") * self.size

        return string[:-1]
