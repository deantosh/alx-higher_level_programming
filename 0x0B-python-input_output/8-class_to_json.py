#!/usr/bin/python3
"""
Module defines a function that returns the dictionary description with
simple data structure for JSON serialization of an object.

Requirements:
 - obj is an instance of a Class
 - All attributes of the obj Class are serializable: list, dictionary, string,
   integer and boolean
"""


def class_to_json(obj):
    """converts class to JSON"""

    obj_dict = {}

    # get list object attributes
    attr_dict = obj.__dict__

    for key, value in attr_dict.items():
        if isinstance(value, (list, dict, str, int, bool)):
            obj_dict[key] = value
    return obj_dict
