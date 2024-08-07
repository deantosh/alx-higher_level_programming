#!/usr/bin/python3
"""
Script defines a function that checks if an object is an instance of a class
or an inherited class.
"""


def is_kind_of_class(obj, a_class):
    """
      returns:
              - True (if an instance of a class or class it inherits from)
              - False (if not)
    """
    return (isinstance(obj, a_class))
