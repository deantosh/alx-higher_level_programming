#!/usr/bin/python3
"""
This module defines a function that appends a string at the end of a text file
(UTF8).

Requirements:
 - If the file doesn’t exist, it should be created
 - You must use the with statement
 - You don’t need to manage file permission or file doesn't exist exceptions.
"""


def append_write(filename="", text=""):
    """
      return:
             number of characters written
    """
    with open(filename, "a", encoding="utf-8") as file:
        num_bytes = file.write(text)
        return num_bytes
