#!/usr/bin/python3
"""
Tests for ``max_integer()`` function that takes in a list and returns maximum
integer in that list.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test cases"""

    def test_empty_list(self):
        self.assertIsNone(max_integer())

    def test_valid_list(self):
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([5, 1, 6, 3]), 6)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([10, -5, 20, -30, 15]), 20)
        self.assertEqual(max_integer([4, 1, 6, 9]), 9)
