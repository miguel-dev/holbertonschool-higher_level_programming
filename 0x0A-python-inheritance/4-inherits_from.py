#!/usr/bin/python3
"""Module only subclass of"""


def inherits_from(obj, a_class):
    """Evaluates if an instance of a subclass of a given class"""
    return isinstance(obj, a_class) and not type(obj) == a_class
