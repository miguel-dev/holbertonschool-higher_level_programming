#!/usr/bin/python3
"""Module Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Defines class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """User friendly representation of class Rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.x,
                                                                 self.y,
                                                                 self.width,
                                                                 self.height)

    def area(self):
        """Calculates the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the instance to stdout with #"""
        print("\n" * self.y, end="")
        for row in range(self.height):
                print(" " * self.x, end="")
                print("#" * self.width)

    def update(self, *args, **kwargs):
        """Updates the class Rectangle for each attribute"""
        number_args = 0
        name_args = ["id", "width", "height", "x", "y"]
        if args and args != []:
            for arg in args:
                setattr(self, name_args[number_args], arg)
                number_args += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
