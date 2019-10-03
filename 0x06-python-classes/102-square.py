#!/usr/bin/python3
class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initiates fields of Square."""
        self.size = size

    def __eq__(self, square_2):
        """Checks if two squares are equal"""
        if self.__size == square_2.size:
            return True
        else:
            return False

    def __ne__(self, square_2):
        """Checks if two squares are not equal"""
        if self.__size != square_2.size:
            return True
        else:
            return False

    def __gt__(self, square_2):
        """Checks if one squares is greater than another"""
        if self.__size > square_2.size:
            return True
        else:
            return False

    def __ge__(self, square_2):
        """Checks if one square is greater of equal to another"""
        if self.__size >= square_2.size:
            return True
        else:
            return False

    def __lt__(self, square_2):
        """Checks if one square is lesser than another"""
        if self.__size < square_2.size:
            return True
        else:
            return False

    def __le__(self, square_2):
        """Checks if one square is less or equal to another"""
        if self.__size <= square_2.size:
            return True
        else:
            return False

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
