#!/usr/bin/python3
"""script: adds all arguments to a python list
   and save them to a file.
"""


import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        # get data from JSON file
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []

    # add items to list if provided
    my_list.extend(sys.argv[1:])

    # save list to JSON file
    save_to_json_file(my_list, "add_item.json")
