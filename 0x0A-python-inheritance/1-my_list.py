#!/usr/bin/python3
"""Contains `MyList` that inherits from list"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Attributes:
        Inherits all attributes from the built-in list class.

    Methods:
        print_sorted(): Prints the elements of the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.

        Returns:
            None
        """
        print(sorted(self))
