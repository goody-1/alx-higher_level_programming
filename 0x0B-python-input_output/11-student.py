#!/usr/bin/python3
"""
Contains class Student that defines student based on '10-student.py'
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

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of a Student instance"""

        if attrs is None:
            return self.__dict__

        new_dict = {}

        for k, v in self.__dict__.items():
            if k in attrs:
                new_dict.update({k: v})

        return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""

        for key, value in json.items():
            setattr(self, key, value)
