#!/usr/bin/python3
"""
Contains the class - BaseGeometry, based on 6-base_geometry.py
"""


class BaseGeometry():
    """
    contains the methods - area and integer_validator
    """

    def area(self):
        """Raises an Exception
        """
        raise Exception("area() is not implementned")

    def integer_validator(self, name, value):
        """validates that 'value' is always an integer
        """
        self.name = name

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))

        self.value = value
