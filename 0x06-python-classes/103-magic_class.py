#!/usr/bin/python3
"""This module contains a class to be conformed to a given python bytecode
"""
import math



class MagicClass():
    """This is a class to test for byte code

    Attributes:
        __radius (int or float): The radius of the circle

    Methods:
        __init__(self, radius=0): Initializing the instance of the class
        area(self): Return the area of the circle
        circumference(self): Return the circumference of the circle
    """

    def __init__(self, radius=0):
        """Initializing the instance of the class

        Args:
            radius (int or float): The radius of the circle
        Raises:
            TypeError: If radius is not a number
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the circle

        Returns:
            float: The area of the circle
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the circle

        Returns:
            float: The circumference of the circle
        """
        return 2 * math.pi * self.__radius
