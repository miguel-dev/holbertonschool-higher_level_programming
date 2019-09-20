#!/usr/bin/python3


def search_replace(my_list, search, replace):

    if not my_list:
        return None

    new_list = my_list[:]

    for i in my_list:
        if i == search:
            new_list[i] = replace

    return new_list
