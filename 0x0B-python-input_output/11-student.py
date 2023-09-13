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
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the student instance"""
        for name in json:
            if (name == "first_name"):
                self.first_name = json[name]
            if (name == "last_name"):
                self.last_name = json[name]
            if (name == "age"):
                self.age = json[name]
