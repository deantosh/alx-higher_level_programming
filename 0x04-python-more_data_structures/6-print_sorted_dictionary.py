#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # create a list of keys
    keys = list(a_dictionary.keys())
    list.sort(keys)

    # sort dictionary
    for i in keys:
        print("{}: {}".format(i, a_dictionary[i]))
