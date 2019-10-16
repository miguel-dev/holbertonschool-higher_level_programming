#!/usr/bin/python3
"""Module to serialize an object to JSON"""

import json


def to_json_string(my_obj):
    """Returns a JSON representation of an object"""
    return json.dumps(my_obj)
