#!/usr/bin/python3
"""module: defines  a function that writes an object to
   a text file using JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """writes JSON string into a file"""
    with open(filename, "w") as file_obj:
        str_rep = json.dumps(my_obj)
        file_obj.write(str_rep)
