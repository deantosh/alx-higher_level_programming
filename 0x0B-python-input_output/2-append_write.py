#!/usr/bin/python3

def append_write(filename="", text=""):
    with open(filename, "a+") as file_obj:
        n_bytes = file_obj.write(text)
        return (n_bytes)
