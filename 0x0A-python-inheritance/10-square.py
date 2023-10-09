#!/usr/bin/python3
"""Defines a Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square:
    """Square class"""
    def __init__(self, size):
        """Instantiation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
