#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """initializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """gets the dictionary description of an object,
           if attrs is a list of strings, retrieves only the
           attributes in this list else retrieve all attributes.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return self.__dict__
