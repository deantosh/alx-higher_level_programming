#!/usr/bin/python3
"""Converts an object into a JSON string"""
import json


def to_json_string(my_obj):
    """return:
              json string
    """
    return json.dumps(my_obj)
