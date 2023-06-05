#!/usr/bin/python3
"""Task_5-rectangle
"""


class Rectangle:
    """Rectgle class defination."""

    def __init__(self, width=0, height=0):
        """Rectangle instance.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """representation of rectangle (#).
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        rectangle_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle_str += '#'
            rectangle_str += '\n'
        return rectangle_str[:-1]

    def __repr__(self):
        """representation of a Rectangle instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """angle instance."""
        print("Bye rectangle...")

    @property
    def width(self):
        """of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """ of a Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ht of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ of a Rectangle instance
        """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter of a Rectangle instance
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
""" End """
