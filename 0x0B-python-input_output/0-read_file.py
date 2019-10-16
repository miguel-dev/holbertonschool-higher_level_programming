#!/usr/bin/python3
"""Module read file"""


def read_file(filename=""):
    """Reads a text file in UTF8 and prints to stdout"""
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end="")
