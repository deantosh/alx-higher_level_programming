#!/usr/bin/python3
"""Module:
          defines a function  that check if an object is an instance of a class
          inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """Return:
              True: if object is instance
              False: if not
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
