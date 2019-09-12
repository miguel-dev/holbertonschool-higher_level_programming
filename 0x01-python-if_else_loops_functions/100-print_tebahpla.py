#!/usr/bin/python3
for c in reversed(range(96, 123)):
    if (c % 2 == 0):
        ascii_code = c
    else:
        ascii_code = c - 32
    print("{}".format(chr(ascii_code)), end="")
