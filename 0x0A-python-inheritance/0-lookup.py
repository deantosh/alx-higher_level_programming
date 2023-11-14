#!/usr/bin/python3
"""Module gets an object's list of attribute and methods"""


def lookup(obj):
    """return:
              list of available attributes and methods of an object
    """
    return dir(obj)
