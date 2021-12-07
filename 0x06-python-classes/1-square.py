#!/usr/bin/python3

"""This module contains a class - Square
"""


class Square():
    """Square class with private attribute - size

    methods:
        set_size - sets the size of the square
        get_size - gets the size of the square
    """

    def __init__(self, size):
        self.__size = size

    def set_size(self, size):
        self.__size = size

    def get_size(self):
        return self.__size
