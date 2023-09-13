#!/usr/bin/python3
import json
"""module: defines a function that returns tthe dictionary with simple
   data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """returns:
              dictionary description of object
    """
    return obj.__dict__
