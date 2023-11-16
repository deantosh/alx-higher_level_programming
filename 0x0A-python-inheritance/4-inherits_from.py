#!/usr/bin/python3
"""Module checks if object is an instances of a class inherited
   directly or indirectly for a specified class
"""


def inherits_from(obj, a_class):
    """return:
              True or False
    """
    if issubclass(type(obj), a_class):
        if type(obj) == a_class:
            return False
        return True
    return False
