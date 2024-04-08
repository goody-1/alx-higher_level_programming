#!/usr/bin/python3
"""A Rectangle class based on 6-rectangle.py file
Adds print_symbol class attribute to the Rectangle class
"""


class Rectangle:
    """Represents a 2D rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle with a width and height.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """Print message on delete of rectangle instance"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height value.

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        """string representation of the rectangle"""
        if self.print_symbol:
            __symbol = self.print_symbol
        else:
            __symbol = type(self).print_symbol
        text = ""

        if self.__width != 0 and self.__height != 0:
            text = (f"{__symbol}" * self.__width + "\n") * (
                self.__height - 1) + (f"{__symbol}" * self.__width)

        return text

    def __repr__(self) -> str:
        """Return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
