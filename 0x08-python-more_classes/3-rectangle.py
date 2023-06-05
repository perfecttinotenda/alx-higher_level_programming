#!/usr/bin/python3
"""
Task-3
Defines Rectangle class.
"""


class Rectangle:
    """Rectangle class body. """

    def __init__(self, width=0, height=0):
        """Initializes Rectangle props in contructor.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Returns informal string representation
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        record_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                record_str += '#'
            record_str += '\n'
        return record_str[:-1]

    @property
    def width(self):
        """Retrieves  width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of a Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle instance
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and return  the perimeter of a Rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
""" End """
