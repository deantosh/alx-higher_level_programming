#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    list_result = my_list[:]
    list_len = len(list_result)
    i = 0

    while i < list_len:
        if (list_result[i] % 2) == 0:
            list_result[i] = True
        else:
            list_result[i] = False
        i += 1

    return list_result
