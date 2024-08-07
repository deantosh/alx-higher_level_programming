#!/usr/bin/python3
"""
Module contains a function that prints a square.
"""


def print_square(size):
    """returns:
                square
    """

    # validate input
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        for col in range(size):
            print('#', end="")
        print("")
