#!/usr/bin/python3
"""
4-print_square Module for printing a square
"""


def print_square(size):
    """Prints square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for r in range(size):
        print("#" * size)
