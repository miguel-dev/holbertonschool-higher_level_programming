#!/usr/bin/python3
"""Module class to JSON"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object"""
    return obj.__dict__
