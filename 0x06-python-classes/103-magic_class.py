#!/usr/bin/python3
"""This module contains a class to be conformed to a given python bytecode
"""
import math


class MagicClass():
    """This is a class to test for byte code
    """

    def __init__(self, radius=None):
        """Initializing the instance of the class"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference"""
        return 2 * math.pi * self.__radius
