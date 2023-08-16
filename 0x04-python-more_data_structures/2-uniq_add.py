#!/usr/bin/python3
def uniq_add(my_list=[]):
    # create an empty list
    new_list = []
    res = 0

    # create a unique list
    for i in my_list:
        if i not in new_list:
            new_list.append(i)

    # add the values in the new list.
    for i in new_list:
        res = res + i

    return res
