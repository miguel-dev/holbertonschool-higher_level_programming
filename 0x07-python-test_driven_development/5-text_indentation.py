#!/usr/bin/python3
"""
Module 5-text_indentation for text indentation
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    fragments = text.split(".")
    new_text = ""
    length = len(fragments)
    for s in range(length):
        new_text += fragments[s].strip()
        if s != length - 1:
            new_text += ".\n\n"

    fragments = new_text.split("?")
    new_text = ""
    length = len(fragments)
    for s in range(length):
        new_text += fragments[s].strip()
        if s != length - 1:
            new_text += "?\n\n"

    fragments = new_text.split(":")
    new_text = ""
    length = len(fragments)
    for s in range(length):
        new_text += fragments[s].strip()
        if s != length - 1:
            new_text += ":\n\n"

    print(new_text, end="")
