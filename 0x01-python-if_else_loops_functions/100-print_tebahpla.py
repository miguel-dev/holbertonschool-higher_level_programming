#!/usr/bin/python3
for c in reversed(range(97, 123)):
    if (c % 2):   #Evaluates if it's even
        c -= 32
    print("{}".format(chr(c)), end="")
