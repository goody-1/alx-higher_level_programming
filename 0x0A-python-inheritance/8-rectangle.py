#!/usr/bin/python3
"""
Contains the class - BaseGeometry, based on 7-base_geometry.py
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry class
    """

    def __init__(self, width, height):
        """Initializes object
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
