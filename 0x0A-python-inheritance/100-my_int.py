#!/usr/bin/python3
"""Contains the class MyInt"""


class MyInt(int):
    """A class that inherits from int but \
    inverts the behaviour of the equality and inequality operators
    """

    def __eq__(self, other):
        """Inverts the behaviour of the equality operator =="""
        return int(self) != int(other)

    def __ne__(self, other):
        """Inverts the behaviour of the inequality operator !="""
        return int(self) == int(other)
