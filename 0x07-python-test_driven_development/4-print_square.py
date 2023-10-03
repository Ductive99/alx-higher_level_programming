#!/usr/bin/python3
"""module defines a function"""


def print_square(size):
    """function that prints a square using # symbol"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print()
