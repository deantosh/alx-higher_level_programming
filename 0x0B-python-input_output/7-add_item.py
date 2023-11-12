#!/usr/bin/python3
"""Module adds command args to a python list"""


import sys

if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = \
        __import__("6-load_from_json_file").load_from_json_file

    filename = "add_item.json"
    arg_list = sys.argv[1:]

    try:
        # get object from json file
        obj = load_from_json_file(filename)

    except FileNotFoundError:
        obj = []

    obj.extend(arg_list)
    # save the obj to json file
    save_to_json_file(obj, filename)
