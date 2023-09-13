#!/usr/bin/python3
"""module: defines a class-to-JSON function"""


def class_to_json(obj):
    """returns:
              a dictionary representation with simple data structure
    """
    return obj.__dict__
