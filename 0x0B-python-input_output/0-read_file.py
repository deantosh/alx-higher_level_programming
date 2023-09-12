#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, "r") as file_obj:
        read_data = file_obj.read()
        print(read_data)
