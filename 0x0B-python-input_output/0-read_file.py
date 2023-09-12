#!/usr/bin/python3
"""defines a function that reads a text file"""


def read_file(filename=""):
    """opens text file to read content"""
    with open(filename, "r", encoding="UTF8") as file_obj:
        read_data = file_obj.read()
        print(read_data, end="")
