#!/usr/bin/python3
"""max_integer() unit test"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMax(unittest.TestCase):
    def test_positve(self):
        e1 = [12, 34, 43, 8, 9, 45]
        self.assertEqual(max_integer(e1), 45)
    
    def test_negative(self):
        e1 = [-12, -34, -43, -8, -9, -45]
        self.assertEqual(max_integer(e1), -8)

    def test_non_int(self):
        string = "Test"
        self.assertEqual(max_integer(string), 't')


if __name__ == "__main__":
    unittest.main()
