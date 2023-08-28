#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        num_int = 0
        for value in my_list:
            if count == x:
                break
            x = isinstance(value, int)
            if x:
                print("{:d}".format(value), end="")
                num_int += 1
            count += 1
        print()
        return num_int
    except indexError:
        print("IndexError: list index out of range")
