#!/usr/bin/python3
for d1 in range(0, 9):
    for d2 in range(1, 10):
        if d1 != d2 and d1 < d2:
            if d1 != 8 or d2 != 9:
                print("{:d}{:d}".format(d1, d2), end=", ")
            else:
                print("{:d}".format(89))
