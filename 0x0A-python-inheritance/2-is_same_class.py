#!/usr/bin/python3
"""Module checks if object is an instance of a specified class"""


def is_same_class(obj, a_class):
    """return:
              True if instance
              False if not
    """
    if type(obj) == a_class:
        return True
    else:
        return False
