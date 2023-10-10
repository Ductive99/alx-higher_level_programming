#!/usr/bin/python3
"""defines a JSON custom function"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a file

    Args:
        my_obj (obj): object
        filename (str): the name of the file
    """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
