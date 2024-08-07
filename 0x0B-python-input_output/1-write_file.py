#!/usr/bin/python3
"""
Module defines a function that writes a string to a text file (UTF8).

Requirements:

 - You must use the with statement
 - You don’t need to manage file permission exceptions.
 - Your function should create the file if doesn’t exist.
 - Your function should overwrite the content of the file if it already exists.
"""


def write_file(filename="", text=""):
    """returns:
               number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        num_bytes = file.write(text)
        return num_bytes
