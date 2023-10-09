#!/usr/bin/python3
"""
Module that defines the is_same_class() function
"""


def is_same_class(obj, a_class):
    """returns whether an object is an instance of the specified class"""
    return (type(obj) is a_class)
