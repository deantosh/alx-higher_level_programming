#!/usr/bin/python3
"""
Module has a function `add_integer()` that adds 2 integers.

Requirements:
  - Prototype: def add_integer(a, b=98):
  - a and b must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer or b must be an integer
  - a and b must be first casted to integers if they are float
  - Returns an integer: the addition of a and b
  - You are not allowed to import any module
"""


def add_integer(a, b=98):
    """returns sum of two numbers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
