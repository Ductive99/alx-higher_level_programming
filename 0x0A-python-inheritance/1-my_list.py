#!/usr/bin/python3
"""Module that defines MyList Class"""


class MyList(list):
    """list subclass"""
    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the list in sorted order"""
        print(sorted(self))
