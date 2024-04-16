#!/usr/bin/python3
"""
Module defines a function that creates an object from a JSON file.

Requirements:
 - You must use the with statement
 - You don’t need to manage exceptions if the JSON string doesn’t
   represent an object.
 - You don’t need to manage file permissions / exceptions.
"""
import json


def load_from_json_file(filename):
    """convert string from JSON file to a python object"""
    with open(filename, "r") as file:
        return json.load(file)
