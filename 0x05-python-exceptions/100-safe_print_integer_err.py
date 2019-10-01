#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    is_integer = False
    try:
        print("{:d}".format(value))
        is_integer = True
    except (ValueError, TypeError) as error:
        print("Exception:", error, file=sys.stderr)
        is_integer = False
    return is_integer
