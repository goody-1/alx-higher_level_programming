#!/usr/bin/python3
"""
Module contains a class MyList
"""


class MyList(list):
    """inherits from list"""

    def print_sorted(self):
        """This function prints the list but sorted in ascending order
        """
        print(sorted(self))
