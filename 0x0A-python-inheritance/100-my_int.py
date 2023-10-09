#!/usr/bin/python3
"""Defines an inherited int class"""


class MyInt(int):
    """Inheriting class"""

    def __eq__(self, value):
        """turn == into !="""
        return self.real != value

    def __ne__(self, value):
        """turn != into =="""
        return self.real == value
