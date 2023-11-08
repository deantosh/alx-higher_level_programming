#!/usr/bin/python3
"""Save object to a json file"""
to_json_string = __import__("3-to_json_string").to_json_string


def save_to_json_file(my_obj, filename):
    """return:
              None
    """
    # convert obj to str
    my_str = to_json_string(my_obj)

    with open(filename, "w", encoding="utf-8") as a_file:
        a_file.write(my_str)
