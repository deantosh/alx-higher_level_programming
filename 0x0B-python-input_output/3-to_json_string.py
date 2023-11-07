#!/usr/bin/python3
"""Converts an object into a JSON string"""


import json
def to_json_string(my_obj):
    """return:
              json string
    """
    my_str = json.dumps(my_obj)
    return my_str
