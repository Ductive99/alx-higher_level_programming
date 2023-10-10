#!/usr/bin/python3
"""defines a JSON custom function"""
import json


def to_json_string(my_obj):
    """returns JSON representation of an object (string)

    Args:
        my_obj: (object)

    Returns:
        JSON representation
    """
    return json.dumps(my_obj)
