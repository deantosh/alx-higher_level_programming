#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # create a copy of list
    new_list = my_list[:]
    lens = len(new_list)

    for i in range(lens):
        if new_list[i] == search:
            new_list[i] = replace

    return new_list
