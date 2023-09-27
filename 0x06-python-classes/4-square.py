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
        self.__size = size

    def area(self):
        """computes square area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
