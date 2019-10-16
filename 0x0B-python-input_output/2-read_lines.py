#!/usr/bin/python3
"""Module for reading n lines"""


def read_lines(filename="", nb_lines=0):
    """Read n lines of a text file and print to stdout"""
    with open(filename, mode="r", encoding="UTF-8") as f:
        n = 0
        if nb_lines <= 0:
            print(f.read(), end="")
        for line in f:
            n += 1
            if (n < nb_lines or nb_lines >= n):
                print(line, end="")
