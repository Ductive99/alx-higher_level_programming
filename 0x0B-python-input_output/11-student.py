#!/usr/bin/python3
"""Defines a Student Class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Student instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retursn dictionary description of the Student"""
        return self.__dict__
