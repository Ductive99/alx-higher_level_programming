#!/usr/bin/python3
"""Defines add_attribute() function"""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object if it's possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
