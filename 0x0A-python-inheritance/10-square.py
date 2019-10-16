#!/usr/bin/python3
"""Module Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square"""
    def __init__(self, size):
        """Validates and initializes data"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates area"""
        return self.__size ** 2
