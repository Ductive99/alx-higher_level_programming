#!/usr/bin/python3
"""
Module that defines the class Rectangle
Rectangle Attributes:
    width -
    height -
    x - x-axis (horizontal) position
    y - y-axis (vertical) position
    id -
Rectangle Methods:
    area - returns rectangle area
    display - prints rectangle using '#'
    __str__ - prints info on the rectangle
    update - update the given argument attributes
"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
            x (int): x-axis position. Defaults to 0.
            y (int): y-axis position. Defaults to 0.
            id (int): instance id. Defaults to number of objects.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter: width
        return: rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter: width
        Sets and Checks the input of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter: height
        return: rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter: height
        Sets and Checks the input of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter: x
        return: x-position of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter: x
        Sets and Checks the input of x-position
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter: y
        return: y-position of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter: y
        Sets and Checks the input of y-position
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Computes rectangle area
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the rectangle instance using the # symbol
        Taking the rectangle's position into account
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """
        Rectangle string representation
        Simple text for the user
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update the rectangle instance

        Argument order is important:
        - 1st arg ->     id
        - 2nd arg ->  width
        - 3rd arg -> height
        - 4th arg ->      x
        - 5th arg ->      y
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]

        if args:
            return

        attribute_map = {
            "id": "id",
            "width": "width",
            "height": "height",
            "x": "x",
            "y": "y",
        }

        for k, v in kwargs.items():
            if k in attribute_map:
                setattr(self, attribute_map[k], v)

    def to_dictionary(self):
        """Returns a dictionnary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y,
        }
