#!/usr/bin/python3
"""defines a JSON custom function"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file

    Args:
        filename (str): the name of the file
    """
    with open(filename, encoding="UTF-8") as f:
        return json.load(f)
