#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    val = my_list[0]

    for i in my_list:
        if i > val:
            val = i
    return val
