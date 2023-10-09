#!/usr/bin/python
"""Module that define a geometry class"""


class BaseGeometry:
    """Geometry Class"""
    def area(self):
        """will return area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates Input"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
