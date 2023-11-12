#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """return:
              None
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
