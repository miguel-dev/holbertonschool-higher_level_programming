#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    is_integer = False
    try:
        print("{:d}".format(value))
        is_integer = True
    except ValueError:
        sys.stderr.write("Exception: Unknown format code 'd' \
                         for object of type 'str'\n")
        is_integer = False
    return is_integer
