#!/usr/bin/python3
"""
Script defines a function that returns `True` if the object is exactly an
instance of the specified class
"""


def is_same_class(obj, a_class):
    """returns:
                - True (if is instance of a class)
                - False (if not)
    """
    return isinstance(type(obj), a_class)
