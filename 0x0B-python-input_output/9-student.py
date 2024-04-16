#!/usr/bin/python3
"""
Contains class Student that defines student
"""


class Student():
    """
    Methods:
        __init__ -> initialize object
        to_json -> retrieves dictionary representation fo a Student instance
    """

    def __init__(self, first_name, last_name, age):
        """Initialize object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of a Student instance"""
        return self.__dict__
