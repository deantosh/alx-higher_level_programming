#!/usr/bin/python3
def safe_print_integer(value):
    try:
        x = isinstance(value, int)
        if x:
            print("{:d}".format(value), end="\n")
            return True
        else:
            return False
    except typeError:
        print("Error: invalid value")
