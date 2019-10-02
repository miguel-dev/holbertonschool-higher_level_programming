#!/usr/bin/python3
class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initiates fields of Square."""
        self.position = position
        self.size = size

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
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position"""
        if (not isinstance(value, tuple) or
           len(value) != 2 or
           not isinstance(value[0], int) or
           not isinstance(value[1], int) or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square in stdout with #"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
