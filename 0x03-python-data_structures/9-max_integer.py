#!/usr/bin/python3


def max_integer(my_list=[]):
    maxx = 0

    if not my_list:
        return None
    for i in my_list:
        if i > maxx:
            maxx = i
    return maxx
