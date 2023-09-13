#!/usr/bin/python3
"""This module defines a student class"""


class Student:
    """initializes student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student
           instance.
        """
        # create a new dict
        my_dict = {}

        if (attrs):
            for name in attrs:
                for key in self.__dict__:
                    if name == key:
                        my_dict.update({key: self.__dict__[key]})
            return my_dict
        else:
            return self.__dict__
