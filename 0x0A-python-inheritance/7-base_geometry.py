#!/usr/bin/python3
"""Contains the class BaseGeometry"""


class BaseGeometry:
    """A base class for geometry operations.

    Methods:
        area(self) -- Raises an Exception with the message
                        'area() is not implemented'
    """

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates `value` as an integer greater than 0.

        Parameters:
        name (str): The name of the variable to validate.
        value (int): The value
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
