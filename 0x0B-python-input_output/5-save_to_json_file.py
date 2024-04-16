#!/usr/bin/python3
"""
Module defines a function that writes an object to a text file, using a JSON
representation.

Requirements:
 - You must use the with statement
 - You don’t need to manage exceptions if the object can’t be serialized.
 - You don’t need to manage file permission exceptions.
"""
import json


def save_to_json_file(my_obj, filename):
    """convert and save to json file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
