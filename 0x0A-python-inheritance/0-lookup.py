#!/usr/bin/python3
"""
Function returns the list of available attributes and methods of an object.
"""


def lookup(obj):
    """returns: a list of attributes and methods"""
    return dir(obj)
