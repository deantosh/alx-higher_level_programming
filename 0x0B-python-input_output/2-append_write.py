#!/usr/bin/python3
"""module: defines a function that appends a string
   at the end of a text file.
"""


def append_write(filename="", text=""):
    """returns:
              nbytes appended to file.
    """
    with open(filename, "a+") as file_obj:
        n_bytes = file_obj.write(text)
        return (n_bytes)
