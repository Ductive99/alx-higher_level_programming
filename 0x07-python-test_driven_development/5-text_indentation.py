#!/usr/bin/python3
"""module defines a function"""


def text_indentation(text):
    """splits a text into multiple lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start_end = True
    for char in text:
        if char in "?.:":
            print(char)
            print()
            start_end = True
        elif char != ' ' or not start_end:
            print(char, end="")
            start_end = False
