#!/usr/bin/python3
"""Module gets the dictionary description of an object"""


def class_to_json(obj):
    """return:
             obj dict
    """
    return obj.__dict__
