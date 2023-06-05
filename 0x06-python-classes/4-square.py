#!/usr/bin/python3
"""Task-4: Square class def"""


class Square:
    """Square class body"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """return new size_square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area_square."""
        return (self.__size * self.__size)
"""The End"""
