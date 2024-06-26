#!/usr/bin/python3
"""
Module defines an empty class ``BaseGeometry``
 - Public instance method: def area(self): that raises an Exception with
   the message area() is not implemented
 - Public instance method: def integer_validator(self, name, value): that
   validates value:
 - you can assume name is always a string
 - if value is not an integer: raise a TypeError exception, with the message
   <name> must be an integer
 - if value is less or equal to 0: raise a ValueError exception with the
   message <name> must be greater than 0
"""


class BaseGeometry:
    """defines a base class"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if type(value) is bool:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
