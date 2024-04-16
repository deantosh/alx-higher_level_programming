#!/usr/bin/python3
"""
Script adds all arguments to a python list, and then save them to a file.

Requirements:
 - You must use your function save_to_json_file from 5-save_to_json_file.py
 - You must use your function load_from_json_file from 6-load_from_json_file.py
 - The list must be saved as a JSON representation in a file named
   add_item.json
 - If the file doesn’t exist, it should be created
 - You don’t need to manage file permissions / exceptions.
"""
import os
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


if len(sys.argv) >= 1:

    # filename
    filename = "add_item.json"

    # check if file exists
    if os.path.exists(filename):
        # load list from file if exists
        arg_list = load_from_json_file(filename)
    else:
        arg_list = []

    # create list to save to file
    script_name = sys.argv[0]
    for arg in sys.argv:
        if script_name == arg:
            continue
        arg_list.append(arg)

    # save to json
    save_to_json_file(arg_list, filename)
