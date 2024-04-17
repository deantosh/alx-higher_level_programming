#!/usr/bin/python3
"""
Script defines a function that inserts a line of text to a file, after each
line containing a specific string.

Requirements:
 - You must use the with statement
 - You don’t need to manage file permission or file doesn't exist exceptions.
 - You are not allowed to import any module
"""


def append_after(filename="", search_string="", new_string=""):
    """appends line after a line conating a specific string"""
    with open(filename, 'r+') as file:
        # move cursor to the beginning of file
        file.seek(0)

        # copy of lines
        lines = file.readlines()

        # clear content in the file
        file.truncate(0)

        # search the line, add the lines
        # add the new_string after line if match is found
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
