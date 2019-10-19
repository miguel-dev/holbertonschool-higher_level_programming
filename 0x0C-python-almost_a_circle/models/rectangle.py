#!/usr/bin/python3
"""Module Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Defines class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance attributes"""
        super().__init__(id)
        __width = width
        __height = height
        __x = x
        __y = y

    @property
    def width(self):
        """Retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width"""
        self.__width = value

    @property
    def height(self):
        """Retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        self.__height = value

    @property
    def x(self):
        """Gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x"""
        self.__x = value

    @property
    def y(self):
        """Gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y"""
        self.__y = value
