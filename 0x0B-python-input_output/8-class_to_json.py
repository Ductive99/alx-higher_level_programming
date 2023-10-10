#!/usr/bin/python3
"""defines custom JSON function"""


def class_to_json(obj):
    """retursn dictionary description with a simple data structure"""
    return obj.__dict__
