#!/usr/bin/python3
"""Module that defines a LockedClass"""


class LockedClass:
    """LockedClass class"""
    def __setattr__(self, name, value):
        if name != "first_name":
            err = f"'LockedClass' object has not atribute '{name}'"
            raise AttributeError(err)
        super().__setattr__(name, value)
