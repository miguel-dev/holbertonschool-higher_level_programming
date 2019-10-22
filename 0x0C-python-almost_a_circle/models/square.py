#!/usr/bin/python3
"""Module Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets size"""
        self.width = value
        self.height = value

    def __str__(self):
        """User friendly representation of a Square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Updates the Square attributes"""
        arg_number = 0
        args_names = ["id", "size", "x", "y"]
        if args and args != []:
            for arg in args:
                setattr(self, args_names[arg_number], arg)
                arg_number += 1
        else:
            for k, v in kwargs.items():
                if k == "size":
                    self.width = v
                    self.height = v
                else:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
