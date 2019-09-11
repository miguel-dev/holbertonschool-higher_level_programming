#!/usr/bin/python3
def uppercase(str):
    for char in str:
        ascii_code = ord(char)
        if ascii_code >= 97 and ascii_code <= 122:
            character = chr(ascii_code - 32)
        else:
            character = char
        print("{}".format(character), end="")
    print()
