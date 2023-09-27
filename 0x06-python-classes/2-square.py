#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Square representation
    Attributes:
        __size (int): square side size
    """
    def __init__(self, size=0):
        """Square initialization
        Args:
            size (int): square side size
        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
