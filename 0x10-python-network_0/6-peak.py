#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    max = 0
    for i in list_of_integers:
        if i > max:
            max = i
    return max
