import unittest
import sys
sys.path.append("../..")
from models.rectangle import Rectangle
"""
Module that defines unittests for rectangle.py.
"""


class TestRectangle_Instantiation(unittest.TestCase):
    """Instantiation unittest for class Rectangle"""

    def test_size_input(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.area(), r2.area())
        self.assertEqual(r1.width + r1.height, r2.width + r2.height)
        self.assertEqual(r1.id, r2.id - 1)

    def test_no_position_input(self):
        r1 = Rectangle(5, 2)
        r2 = Rectangle(4, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r1.id, r2.id - 1)

    def test_position_input(self):
        r1 = Rectangle(12, 3, 4, 5)
        r2 = Rectangle(21, 4, 5, 4)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r1.id, r2.id - 1)

    def test_position_input_area(self):
        r1 = Rectangle(12, 3, 4, 5)
        r2 = Rectangle(21, 4, 5, 4)
        self.assertEqual(r1.area(), 36)
        self.assertEqual(r2.area(), 84)
        self.assertEqual(r1.id, r2.id - 1)

    def test_incorrect_width(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 2)

    def test_incorrect_width(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10.77, 2)

    def test_incorrect_width_list(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle([12, 2], 2)

    def test_incorrect_height(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, "10")

    def test_incorrect_height(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 10.3)

    def test_incorrect_height_tuple(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, (12, ))

    def test_incorrect_x(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, "1")

    def test_incorrect_x_float(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 1.5)

    def test_incorrect_x_dict(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, {"x": 1})

    def test_incorrect_y(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 1, "1")

    def test_incorrect_y_float(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 1, 1.1)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 7)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(77, 0)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(7, 0)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 2, -1, 5)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(3, 2, 0, -1)

    def test_no_input(self):
        with self.assertRaises(TypeError):
            r = Rectangle()


class TestRectangle_Assignment(unittest.TestCase):
    """Assignment unittest for class Rectangle"""
    def test_assign_size(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        r2.width, r2.height = 1, 2
        self.assertEqual(r1.area(), r2.area())

    def test_bad_size_assignment(self):
        r = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            r.width = -1

    def test_bad_size_assignment2(self):
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.width = "string"

    def test_assign_position(self):
        r1 = Rectangle(1, 2)
        r1.x = 3
        r1.y = 8
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 8)

    def test_bad_position_assignment(self):
        r = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            r.x = -1

    def test_bad_position_assignment2(self):
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.y = {}

    def test_assign_id(self):
        r1 = Rectangle(9, 2)
        r2 = Rectangle(2, 3, 0, 0, 12)
        r3 = Rectangle(4, 9)
        self.assertEqual(r1.id, r3.id - 1)
        self.assertEqual(r2.id, 12)

    
class TestRectangle_str(unittest.TestCase):
    """__str__ unittest for class Rectangle"""
    pass # TO-DO


class TestRectangle_display(unittest.TestCase):
    """display() unittest for class Rectangle"""
    pass # TO-DO


class TestRectangle_update(unittest.TestCase):
    """update() unittest for class Rectangle"""
    pass # TO-DO


if __name__ == "__main__":
    unittest.main()
