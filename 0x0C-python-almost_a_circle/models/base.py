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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as file:
            if list_objs is None:
                file.write("[]")
                return
            file.write("[")
            for obj in range(len(list_objs)):
                dictionary = list_objs[obj].to_dictionary()
                json_string = cls.to_json_string(dictionary)
                file.write(json_string)
                if obj != len(list_objs) - 1:
                    file.write(", ")
            file.write("]")

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of a list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)
