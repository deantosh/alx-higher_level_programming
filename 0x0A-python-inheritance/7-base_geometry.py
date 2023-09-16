#!/usr/bin/python3
"""Module: defines base class BaseGeometry class"""


class BaseGeometry:
    """defines a BaseGeometry class"""

    def area(self):
        """defines area - not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method: validates the integer passed as value"""

        """ raise:
                  TypeError - if not integer
                  ValueError - if less than or equal to zero
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
