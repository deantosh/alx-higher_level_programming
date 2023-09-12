#!/usr/bin/python3

def write_file(filename="", text=""):
    with open(filename, "w") as file_obj:
        num_bytes = file_obj.write(text)
        return (num_bytes)
