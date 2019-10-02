#!/usr/bin/python3
class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initiates fields of Square."""
        self.__size = size

    @property
    def size(self):
        """Retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size"""
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns square area."""
        return self.__size ** 2
