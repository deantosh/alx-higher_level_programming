#!/usr/bin/python3

import sys

if __name__ == "__main__":

    result = 0

    for i in sys.argv:
        if i == "./3-infinite_add.py":
            continue
        result += int(i)

    print("{}".format(result))
