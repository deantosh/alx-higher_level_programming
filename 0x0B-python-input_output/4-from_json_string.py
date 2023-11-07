#!/usr/bin/python3
"""Converts JSON string into python object"""
import json


def from_json_string(my_str):
    """return:
              python object
    """
    my_obj = json.loads(my_str)
    return my_obj
