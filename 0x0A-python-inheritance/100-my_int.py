#!/usr/bin/python3
"""
Contains class MyInt
"""


class MyInt(int):
    """
    Subclass of int, inverted comparison operators '==' and '!='
    """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
