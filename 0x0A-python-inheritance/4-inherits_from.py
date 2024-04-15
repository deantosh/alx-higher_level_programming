#!/usr/bin/python3
"""
Script defines a function that checks if an instance of a class that inherited
(directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
      Returns:
               - True (if is subclass)
               - False (if not)
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
