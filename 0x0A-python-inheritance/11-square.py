#!/usr/bin/python3
"""
Contains the class - Square, based on 10-square.py
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Inherits from BaseGeometry class
    """

    def __init__(self, size):
        """Initializes object
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
