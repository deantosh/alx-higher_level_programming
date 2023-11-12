#!/usr/bin/python3
"""Read a text file"""


def read_file(filename=""):
    """Reads all the content of the file"""
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")
