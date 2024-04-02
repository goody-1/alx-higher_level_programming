#!/usr/bin/python3

"""This module contains a class - Square
This is based on "4-square" but now makes the instances comparable
"""


class Square():
    """A class representing a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new instance of the Square class.
        area(self): Calculates the area of the square.
        __str__(self): Returns a string representation of the square.
        __eq__(self, other): Checks if the square is equal to another square.
        __lt__(self, other): Checks if the square is less than another square.
        __le__(self, other): Checks if the square is less than or equal to
            another square.
        __gt__(self, other): Checks if the square is greater than
            another square.
        __ge__(self, other): Checks if the square is greater than or equal to
            another square.
        __ne__(self, other): Checks if the square is not equal to
            another square.
    """

    def __init__(self, size=0):
        """Initialize a new instance of the Square class.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return "{}".format(self.area())

    def __eq__(self, other):
        """Check if the square is equal to another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the squares are equal, False otherwise.
        """
        return self.area() == other.area()

    def __lt__(self, other):
        """Check if the square is less than another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the square is less than the other square,
                    False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the square is less than or equal to another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the square is less than or equal to the other square,
                    False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if the square is greater than another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the square is greater than the other square,
                    False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the square is greater than or equal to another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the square is greater than or equal to the other
                    square, False otherwise.
        """
        return self.area() >= other.area()

    def __ne__(self, other):
        """Check if the square is not equal to another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the squares are not equal, False otherwise.
        """
        return self.area() != other.area()
