#!/usr/bin/python3
"""
This module contains a function that reads a file (UTF8) and prints it out to
stdout.

N:B must use ``with`` statement.
"""


def read_file(filename=""):
    """prints contents of the file to stdout"""
    with open(filename, "r") as file:
        contents = file.read()
        print(contents)
