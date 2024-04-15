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
