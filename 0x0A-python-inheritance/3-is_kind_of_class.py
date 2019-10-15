#!/usr/bin/python3
"""Module 3-is_kind_of_class.py"""


def is_kind_of_class(obj, a_class):
    """Evaluates if an object is an instance of a class, or if it's an instance
       of a class that inherited from, the specified class"""
    return isinstance(obj, a_class)
