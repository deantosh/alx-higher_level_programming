#!/usr/bin/python3
"""Module saves object to a json file"""

import json


def save_to_json_file(my_obj, filename):
    """return:
              None
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
