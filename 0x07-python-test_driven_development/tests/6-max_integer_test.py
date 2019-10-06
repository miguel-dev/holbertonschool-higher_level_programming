#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_max_beginning(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_max_middle(self):
        self.assertEqual(max_integer([1, 4, 2]), 4)

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative(self):
        self.assertEqual(max_integer([-1, 1, 2]), 2)

    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

if __name__ == '__main__':
    unittest.main()
