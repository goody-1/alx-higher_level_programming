#!/usr/bin/python3
"""Contains the class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a rectangle

    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle

    Methods:
        area(self) -- Returns the area of the rectangle
        __str__(self) -- Returns a string representation of the
                        Rectangle object
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Rectangle object."""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __init__(self, width, height):
        """
        Initializes a new Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Rectangle object."""
        return f"[Rectangle] {self.__width}/{self.__height}"
