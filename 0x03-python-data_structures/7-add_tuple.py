#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    len_a = len(tuple_a)
    len_b = len(tuple_b)

    i = 0
    j = 0
    x = 0
    y = 0

    while i < len_a:
        if i == 0:
            x = x + tuple_a[i]
        if i == 1:
            y = y + tuple_a[i]
        i = i + 1
    while j < len_b:
        if j == 0:
            x = x + tuple_b[j]
        if j == 1:
            y = y + tuple_b[j]
        j = j + 1

    # create a new tuple
    tuple_c = (x, y)

    return tuple_c
