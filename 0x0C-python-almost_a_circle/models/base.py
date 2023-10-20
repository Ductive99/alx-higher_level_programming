#!/usr/bin/python3
"""Module that define the class Base"""
import json
import os
import csv
import turtle


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor

        Args:
            id (int): instance id. Defaults to __nb_objects' value.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        with open(f"{cls.__name__}.json", 'w') as f:
            f.write(cls.to_json_string([obj.to_dictionary()
                    for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with attributes set"""
        if cls.__name__ == "Square":
            new = cls(1)
        else:
            new = cls(1, 1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = cls.from_json_string(file.read())
                return [cls.create(**item) for item in data]
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes csv of list_objs to a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of instances from a csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                dict_list = csv.DictReader(csvfile, fieldnames=fieldnames)
                dict_list = [dict([k, int(v)] for k, v in d.items())
                             for d in dict_list]
                return [cls.create(**d) for d in dict_list]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw a list of rectangles and a list of squares"""
        t = turtle.Turtle()
        t.screen.bgcolor("black")
        t.pensize(3)
        t.shape("turtle")
        t.color("red")

        for r in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(r.x, r.y)
            t.down()
            for i in range(2):
                t.forward(r.width)
                t.left(90)
                t.forward(r.height)
                t.left(90)
            t.hideturtle()

        t.color("blue")
        for s in list_squares:
            t.showturtle()
            t.up()
            t.goto(s.x, s.y)
            t.down()
            for i in range(4):
                t.forward(s.width)
                t.left(90)
            t.hideturtle()

        t.exitonclick()
