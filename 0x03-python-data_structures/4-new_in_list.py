#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list[:]
    list_len = len(list_copy) - 1

    if idx < 0:
        return my_list

    elif idx > list_len:
        return my_list

    else:
        list_copy[idx] = element
        return list_copy
