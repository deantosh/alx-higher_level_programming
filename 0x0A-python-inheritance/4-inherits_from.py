#!/usr/bin/python3
"""
Script defines a function that checks if an instance of a class that inherited
(directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """Returns true if object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
