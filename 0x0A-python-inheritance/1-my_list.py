#!/usr/bin/python3
"""
Module defines a class ``MyList`` that inherits from list.
"""


class MyList(list):
    """defines a subclass of the list class"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
