#!/usr/bin/python3
"""Module Student to JSON"""


class Student:
    """Defines class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a student instance"""
        if attrs is None:
            return self.__dict__
        d = {}
        for k, v in self.__dict__.items():
            for a in attrs:
                if k == a:
                    d[k] = v
        return d
