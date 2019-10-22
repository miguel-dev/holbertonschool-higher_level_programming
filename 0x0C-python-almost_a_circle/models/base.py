#!/usr/bin/python3
"""Module Base"""

import json


class Base:
    """Defines Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of instance variables"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of a list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
