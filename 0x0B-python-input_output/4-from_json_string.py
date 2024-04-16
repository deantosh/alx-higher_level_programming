#!/usr/bin/python3
"""
Module defines a function that returns an object represented by a JSON string.

Requirement:
 - You don’t need to manage exceptions if the JSON string doesn’t represent
   an object.
"""
import json


def from_json_string(my_str):
    """converts JSON string to python object"""
    return json.loads(my_str)
