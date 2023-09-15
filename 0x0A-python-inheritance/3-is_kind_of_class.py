#!/usr/bin/python3
"""Module: defines a function that check is an obj is an
           instance of a class.
"""


def is_kind_of_class(obj, a_class):
    """Return:
              True - if object is an instance of a class.
              False - if not an instance.
    """
    return isinstance(obj, a_class)
