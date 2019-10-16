#!/usr/bin/python3
"""Module MyInt"""


class MyInt(int):
    """Definition of MyInt"""
    def __init__(self, number):
        """Initializes the number"""
        self.__number = number

    def __eq__(self, other):
        """Redefined equal comparison operator"""
        if self.__number == other:
            return False
        else:
            return True

    def __ne__(self, other):
        """Redefined not equal comparison operator"""
        if self.__number != other:
            return False
        else:
            return True
