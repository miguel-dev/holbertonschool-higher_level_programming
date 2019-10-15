#!/usr/bin/python3
"""Module Geometry"""


class BaseGeometry:
    """Definition of BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if not type(value) == int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Definition of Rectangle"""
    def __init__(self, width, height):
        """Initializes and validates data"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """User friendly representation of a Rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """Calculates the area"""
        return self.__width * self.__height


class Square(Rectangle):
    def __init__(self, size):
        """Validates and initializes data"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates area"""
        return self.__size ** 2
