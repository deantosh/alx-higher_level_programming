#!/usr/bin/python3
"""Module: defines a function that returns  a list
   of object attributes.
"""


def lookup(obj):
    """Return:
               a list of available attributes and methods of an object
    """
    return dir(obj)
