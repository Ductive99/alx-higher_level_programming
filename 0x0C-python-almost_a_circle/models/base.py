#!/usr/bin/python3
"""Module that define the class Base"""


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor

        Args:
            id (int): instance id. Defaults to __nb_objects' value.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
