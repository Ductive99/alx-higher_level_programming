#!/usr/bin/python3
"""Module that define the class Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        with open(f"{cls.__name__}.json", 'w') as f:
            f.write(cls.to_json_string([obj.to_dictionary()
                    for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with attributes set"""
        new = cls(1, 1)
        new.update(**dictionary)
        return new
