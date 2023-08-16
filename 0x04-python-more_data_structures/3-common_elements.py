#!/usr/bin/python3
def common_elements(set_1, set_2):
    # convert to list
    list_1 = list(set_1)
    list_2 = list(set_2)
    list_3 = list()

    for i in list_1:
        for j in list_2:
            if i == j:
                list_3.append(i);

    # convert back to a set
    set_3 = set(list_3)

    return set_3
