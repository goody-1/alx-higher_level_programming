#!/usr/bin/python3
"""Contains Square class that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a square

    Attributes:
        size (int): The size of the square

    Methods:
        area(self) -- Returns the area of the square
    """

    def __init__(self, size):
        """
        Initializes a new Square.

        Args:
            size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2
