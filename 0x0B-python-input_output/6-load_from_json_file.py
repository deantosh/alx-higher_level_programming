#!/usr/bin/python3
"""module: defines a function tat creates an object
   from a JSON file.
"""
import json


def load_from_json_file(filename):
    """returns:
              object
    """
    with open(filename, "r") as json_file:
        data = json_file.read()
        obj = json.loads(data)
        return (obj)
