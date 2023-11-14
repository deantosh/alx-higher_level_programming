#!/usr/bin/python3
"""Module defines a function that prints a square with the character #"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()

    for i in range(size):
        for i in range(size):
            print("#", end="")
        print()
