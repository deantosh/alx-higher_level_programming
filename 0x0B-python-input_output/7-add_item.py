#!/usr/bin/python3
"""Script adds command args to a python list"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


# create file
filename = "add_item.json"

n = len(sys.argv)

if n > 1:
    # get list of all command line args
    arg_list = sys.argv[1:]

try:
    # get object from json file
    obj = load_from_json_file(filename)
    # add arg list to obj
    obj.extend(arg_list)

except FileNotFoundError:
    obj = []

# save the obj to json file
save_to_json_file(obj, filename)
