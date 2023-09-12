#!/usr/bin/python3
"""module: defines a function that converts an object
   into JSON string representation.
"""
import json


def to_json_string(my_obj):
    """returns:
               string representation
    """
    str_rep = json.dumps(my_obj)
    return (str_rep)
