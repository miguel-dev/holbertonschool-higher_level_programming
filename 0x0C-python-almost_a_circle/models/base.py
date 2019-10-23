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
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as file:
            if list_objs is None:
                file.write([])
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                json_string = cls.to_json_string(dictionary)
                file.write("[" + json_string + "]")
