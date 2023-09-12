#!/usr/bin/python3
"""module: defines a function to write to a file"""


def write_file(filename="", text=""):
    """returns the bytes wrote"""
    with open(filename, "w") as file_obj:
        num_bytes = file_obj.write(text)
        return (num_bytes)
