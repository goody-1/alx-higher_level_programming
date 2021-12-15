#!/usr/bin/python3
"""
Contains a rectangle class based on 4-rectangle.py
"""


class Rectangle():
    """
    A rectangle class
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize object"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """
        Tracks deletion of object
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        """string representation of the rectangle
        Prints the string
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("#" * self.__width + "\n") * (
            self.__height - 1) + "#" * self.__width

    def __repr__(self):
        """Return a string representation of the rectangle to be able to
        recreate an new instance by using eval()"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
