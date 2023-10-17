#!/usr/bin/python3
"""Module that defines the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """class instantiation

        Args:
            size (int): square side length
            x (int): x-axis position. Defaults to 0.
            y (int): y-axis position. Defaults to 0.
            id (int): instance id. Defaults to number of objects*.
                *number of objects that weren't manually set
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter: size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter: size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Simple rectangle information display"""
        return f"[Square] ({self.id}) {self.x}/{self.y} \
- {self.width}"

    def update(self, *args, **kwargs):
        """Update the square instance

        Argument order is important
        - 1st arg ->   id
        - 2nd arg -> size
        - 3rd arg ->    x
        - 4th arg ->    y

        if *args is None:
            *kwargs will be taken into account
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
            return

        attribute_map = {
            "id": "id",
            "x": "x",
            "y": "y",
        }

        for k, v in kwargs.items():
            if k in attribute_map:
                setattr(self, attribute_map[k], v)
            if k == "size":
                self.size = v

    def to_dictionary(self):
        """Returns a dictionnary representation of a Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
        }
