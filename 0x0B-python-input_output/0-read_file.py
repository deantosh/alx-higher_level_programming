#!/usr/bin/python3
"""module: defines a function that reads a text file"""


def read_file(filename=""):
    """prints the read file data"""
    with open(filename, "r") as file_obj:
        read_data = file_obj.read()
        print(read_data, end="")
