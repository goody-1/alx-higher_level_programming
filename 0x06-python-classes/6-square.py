#!/usr/bin/python3

"""This module contains a class - Square
This is based on "5-square" but now prints the square
"""


class Square():
    """A class representing a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square when printed.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes
            a new Square instance.
        area(self): Calculates the area of the square.
        my_print(self): Prints the square.

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize object.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square when printed.
                                Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not
                        a tuple of 2 positive integers.
            ValueError: If size is less than 0.

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
        """Get square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set square size.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Gets the position for the square to be printed."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position for the square to be printed.

        Args:
            value (tuple): The position of the square when printed.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.

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
        """Calculates the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square."""
        if self.__size == 0:
            print()
        elif self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()

        __space_no = self.__position[0] * " "
        for i in range(self.__size):
            print("{}".format(__space_no), end="")
            for j in range(self.__size):
                print("#", end="")
            print()
