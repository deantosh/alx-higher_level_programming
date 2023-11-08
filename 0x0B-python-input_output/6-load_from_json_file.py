#!/usr/bin/python3
"""Creates an object from a json file"""
from_json_string = __import__("4-from_json_string").from_json_string


def load_from_json_file(filename):
    """return:
          None
    """
    with open(filename, "r", encoding="utf-8") as a_file:
        my_str = a_file.read()

        my_obj = from_json_string(my_str)

        return my_obj
