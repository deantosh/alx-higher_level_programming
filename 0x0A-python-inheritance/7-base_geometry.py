#!/usr/bin/python3
"""Module defines BaseGeometry class"""


class BaseGeometry:
    """defines BaseGeometry class"""

    def area(self):
        """defines area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value"""
        if type(value) != int:
            raise TypeError("name must be an integer")
        if value <= 0:
            raise ValueError("name must be greater than 0")

        self.name = value
