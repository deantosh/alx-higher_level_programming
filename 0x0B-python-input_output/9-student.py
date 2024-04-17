#!/usr/bin/python3
"""
Module defines a ``Student`` class.

Requirements:
 - Public instance attributes:
        -> first_name
        -> last_name
        ->age
 - Instantiation with first_name, last_name and age: def __init__(
   self, first_name, last_name, age):
 - Public method def to_json(self): that retrieves a dictionary representation
   of a Student instance (same as 8-class_to_json.py)
 - You are not allowed to import any module
"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """initializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of student object"""
        obj_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (str, int, dict, list, bool)):
                obj_dict[key] = value
        return obj_dict
