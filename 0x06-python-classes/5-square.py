#!/usr/bin/python3
"""Task-5: Square class def"""


class Square:
    """Square class body"""

    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        """Square setter and getter for __size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return th area_square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print stdout the square_character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
"""Tye End"""
