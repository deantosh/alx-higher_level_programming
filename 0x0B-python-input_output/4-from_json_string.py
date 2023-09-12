#!/usr/bin/python3
"""module: defines a function that converts JSON string
   into an object.
"""
import json


def from_json_string(my_str):
    """returns:
              object
    """
    obj = json.loads(my_str)
    return (obj)
