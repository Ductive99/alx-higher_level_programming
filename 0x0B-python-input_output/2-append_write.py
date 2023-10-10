#!/usr/bin/python3
"""defines a file appending function"""


def append_write(filename="", text=""):
    """Append a text to a file

    Args:
        filename (str): the name of the file.
        text (str): the text to write to the file.
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
