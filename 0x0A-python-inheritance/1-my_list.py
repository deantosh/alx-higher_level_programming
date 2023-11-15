#!/usr/bin/python3
"""Defines a class that inherits from list class"""


class MyList(list):
    """creates a list"""

    def print_sorted(self):
        """sort list in ascending order"""
        new_list = self.copy()
        new_list.sort()
        print(new_list)
