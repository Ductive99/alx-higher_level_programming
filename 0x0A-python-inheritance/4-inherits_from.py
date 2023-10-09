#!/usr/bin/python3
"""Module that defines inherits_from()"""


def inherits_from(obj, a_class):
    """
    returns whether the obj is an inherited class
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
