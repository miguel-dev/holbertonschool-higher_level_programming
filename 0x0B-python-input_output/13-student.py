#!/usr/bin/python3
"""Module Student to Disk and Reload"""


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

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for k, v in json.items():
            for key, value in self.__dict__.items():
                if k == key:
                    self.__dict__[k] = v
