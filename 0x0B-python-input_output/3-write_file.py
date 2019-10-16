#!/usr/bin/python3
"""Module for writing to a file"""


def write_file(filename="", text=""):
    """Writes string to a text file and returns number of characters"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
