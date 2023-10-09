#!/usr/bin/python
"""Module that define a geometry class"""


class BaseGeometry:
    """Geometry Class"""
    def area(self):
        """will return area"""
        raise Exception("area() is not implemented")
