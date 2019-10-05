#!/usr/bin/python3
"""
Module 5-text_indentation for text indentation
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()

    text = text.replace(". ", ".\n\n")
    text = text.replace("? ", "?\n\n")
    text = text.replace(": ", ":\n\n")

    print(text, end="")
