#!/usr/bin/python3
"""Module: defines a class that inherits from list"""


class MyList(list):
    """DerivedClass method"""
    def print_sorted(self):
        # create a copy of list
        new_list = self.copy()

        # sort the new_list
        new_list.sort()

        # print new_list
        print(new_list)
