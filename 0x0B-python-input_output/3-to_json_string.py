#!/usr/bin/python3
"""
Module defines a function that returns the JSON representation of an object.

Requirement:
 - You don’t need to manage exceptions if the object can’t be serialized.
"""
import json


def to_json_string(my_obj):
    """converts object to json string"""
    return json.dumps(my_obj)
