#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as file_obj:
        str_rep = json.dumps(my_obj)
        file_obj.write(str_rep)
