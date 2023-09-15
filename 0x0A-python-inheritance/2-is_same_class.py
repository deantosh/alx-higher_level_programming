#!/usr/bin/python3
"""Module: defines a function that checks if an object
   is an instance of a class.
"""


def is_same_class(obj, a_class):
    """ Return:
               True - if object is an instance.
               False - not an instance.
    """
    return type(obj) is a_class
