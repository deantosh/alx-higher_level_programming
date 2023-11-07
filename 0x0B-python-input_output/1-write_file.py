#!/usr/bin/python3
"""Writes a string to a text file"""


def write_file(filename="", text=""):
    """return:
              number of character read
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
