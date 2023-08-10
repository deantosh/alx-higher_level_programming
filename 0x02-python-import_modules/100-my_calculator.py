#!/usr/bin/python3

import sys
from calculator_1 import *

if __name__ == "__main__":

    args = sys.argv
    n = len(args) - 1

    if n != 3:
        print("Usage: {} <a> <operator> <b>".format(args[0]))
        exit(1)

    elif (args[2] == '+' or args[2] == '-' or args[2] == '*' or args[2] == '/'):
        a = int(args[1])
        o = args[2]
        b = int(args[3])

        if o == '+':
            print("{} {} {} = {}".format(a, o, b, add(a, b)))
        if o == '-':
            print("{} {} {}= {}".format(a, o, b, sub(a, b)))
        if o == '*':
            print("{} {} {}= {}".format(a, o, b, mul(a, b)))
        if o == '/':
            print("{} {} {}= {}".format(a, o, b, div(a, b)))
        exit(0)

    else:
        print("Unknown operator. Available operators: +, -, *, /")
        exit(1)
