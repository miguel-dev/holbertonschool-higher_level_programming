#!/usr/bin/python3
"""Module MyList"""


class MyList(list):
    """Definition of MyList"""
    def print_sorted(self):
        """Prints the list in ascending sorted order"""
        new_list = self.copy()
        new_list.sort()
        print(new_list)
