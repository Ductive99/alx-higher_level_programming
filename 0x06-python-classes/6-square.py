#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Square representation"""
    def __init__(self, size=0, position=(0, 0)):
        """Square initialization
        Args:
            size (int): square side size
            position (tuple): square coordinates
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """square position"""
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is tuple and
                len(value) == 2 and
                type(value[0]) is int and
                type(value[1]) is int and
                value[0] < 0 and value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """computes square area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    def my_print(self):
        """prints the square using # symbols"""
        if self.__size == 0:
            print()
            return
        [print() for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print()
