#!/usr/bin/python3
"""Module that define a file reading function"""


def read_file(filename=""):
    """Reads a file and prints its content to stdout

    Args:
        filename (str):  name of the file.
    """
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
