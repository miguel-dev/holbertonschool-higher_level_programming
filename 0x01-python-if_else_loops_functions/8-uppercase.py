#!/usr/bin/python3
def uppercase(str):
    ch = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            ch = chr(ord(char) - 32)
        else:
            ch = char
        print(ch, end="")
    print()
