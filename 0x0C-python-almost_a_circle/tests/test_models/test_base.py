import unittest
import sys
sys.path.append("../..")
from models.base import Base
"""
Module that defines unittests for base.py.
"""


class TestBase(unittest.TestCase):
    """Instantiation unittest for class Base"""

    def test_empty(self):
        a = Base()
        b = Base()
        self.assertEqual(a.id, b.id - 1)

    def test_empty2(self):
        a = Base()
        b = Base()
        c = Base()
        d = Base()
        e = Base()
        f = Base()
        self.assertEqual(a.id + b.id + c.id, d.id + e.id + f.id - 9)

    def test_None(self):
        a = Base(None)
        b = Base(None)
        self.assertEqual(a.id, b.id - 1)

    def test_arg(self):
        a = Base(10)
        self.assertEqual(a.id, 10)

    def test_arg_and_no_arg(self):
        a = Base()
        b = Base(10)
        c = Base()
        self.assertEqual(b.id, 10)
        self.assertEqual(a.id, c.id - 1)

    def test_change_id(self):
        a = Base()
        a.id = 10
        self.assertEqual(a.id, 10)

    def test_change_nb_instances(self):
        with self.assertRaises(AttributeError):
            print(Base(10).__nb_instances)


if __name__ == "__main__":
    unittest.main()
