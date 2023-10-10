#!/usr/bin/python3
"""defines a JSON custom function"""
import json


def from_json_string(my_str):
    """returs an object represented by a JSON string

    Args:
        my_str (string): a string
    """
    return json.loads(my_str)
