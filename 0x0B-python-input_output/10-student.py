#!/usr/bin/python3
"""Defines a Student Class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Student instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retursn dictionary description of the Student"""
        d = self.__dict__.copy()
        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return d
            
            n = {}

            for a in range(len(attrs)):
                for s in d:
                    if attrs[a] == s:
                        n[s] = d[s]
            return n
        return self.__dict__
