#!/usr/bin/python3
"""
Module that defines the lookup function
"""


def lookup(obj):
    """returns list of available attributes and methods of the given object"""
    return dir(obj)
