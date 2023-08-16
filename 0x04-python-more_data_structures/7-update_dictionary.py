#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # if key exists replace its value
    if key in a_dictionary.keys():
        a_dictionary[key] = value

    # if not add
    else:
        a_dictionary[key] = value

    return a_dictionary
