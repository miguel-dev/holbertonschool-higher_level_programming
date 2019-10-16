#!/usr/bin/python3
"""Module Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Definition of Rectangle"""
    def __init__(self, width, height):
        """Initializes and validates data"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
