#!/usr/bin/python3

import hidden_4 as h_file

if __name__ == "__main__":

    list = dir(h_file)

    for n in list:
        if n[:2] == '__':
            continue
        print("{}".format(n))
