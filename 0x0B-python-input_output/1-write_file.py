#!/usr/bin/python3
"""defines a file writing function"""


def write_file(filename="", text=""):
    """Write a text to a file

    Args:
        filename (str): the name of the file.
        text (str): the text to write to the file.
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
