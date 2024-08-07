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
        -> If attrs is a list of strings, only attribute names contained in
           this list must be retrieved.
        -> Otherwise, all attributes must be retrieved
 - Public method def reload_from_json(self, json): that replaces all attributes
   of the Student instance:
        -> You can assume json will always be a dictionary
        -> A dictionary key will be the public attribute name
        -> A dictionary value will be the value of the public attribute
 - You are not allowed to import any module
"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """initializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of student object"""
        obj_dict = {}
        if attrs is None:
            for key, value in self.__dict__.items():
                if isinstance(value, (str, int, dict, list, bool)):
                    obj_dict[key] = value
        else:
            for key in attrs:
                value = getattr(self, key, None)
                if value is None:
                    continue
                if isinstance(value, (str, int, dict, list, bool)):
                    obj_dict[key] = value

        return obj_dict

    def reload_from_json(self, json):
        """replaces values of all attributes of the student instance"""
        for attr_name, value in json.items():
            if attr_name in self.__dict__:
                setattr(self, attr_name, value)
