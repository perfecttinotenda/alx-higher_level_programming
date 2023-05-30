#!/usr/bin/python3
"""Task-3 Square class def."""


class Square:
    """Square class body."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the new area of the square."""
        return (self.__size * self.__size)
"""Tge End"""
