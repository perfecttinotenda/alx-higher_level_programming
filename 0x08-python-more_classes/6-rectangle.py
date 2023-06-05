#!/usr/bin/python3
"""Task_6-rectangle
"""


class Rectangle:
    """Rectass defiation.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """instannce in a contructor.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """f rectangle (#)
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
        """resentation of a Rectangle instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """a rectangle is destroyed"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """idth of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """of a Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """eight of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """of a Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """e area of a Rectangle instance
        """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter of a Rectangle instance
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
""" End """
