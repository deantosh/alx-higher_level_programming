#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """represents a  student"""
    def __init__(self, first_name, last_name, age):
        """intializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """gets the dictionary description of an object"""
        return self.__dict__
