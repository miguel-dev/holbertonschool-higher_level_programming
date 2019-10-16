#!/usr/bin/python3


def number_of_lines(filename=""):
    with open(filename) as f:
        number_lines = 0
        for line in f:
            number_lines += 1
        return number_lines
