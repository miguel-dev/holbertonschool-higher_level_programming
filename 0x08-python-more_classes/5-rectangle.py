#!/usr/bin/python3
"""
Module Rectangle
"""


class Rectangle:
    """Definition of a rectangle."""
    def __init__(self, width=0, height=0):
        """Initializes instance variables."""
        self.__width = width
        self.__height = height

    def __del__(self):
        """Used when an object Rectangle has been garbage collected."""
        print("Bye rectangle...")

    def __str__(self):
        """User friendy representation of a rectangle."""
        height = self.__height
        width = self.__width
        string = ""
        for i in range(height):
            string += "#" * width
            if i != height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """Canonical representation of a rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns rectangle perimeter"""
        perimeter = 0
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
