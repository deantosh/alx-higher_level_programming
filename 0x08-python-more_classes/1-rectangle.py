#!/usr/bin/python3
"""
This module defines a ``rectangle`` class.

Requirements:
 1. Private instance attribute: width:
       - property def width(self): to retrieve it
       - property setter def width(self, value): to set it:
              - width must be an integer, otherwise raise a TypeError exception
                with the message width must be an integer
              - if width is less than 0, raise a ValueError exception with the
                message width must be >= 0
 2. Private instance attribute: height:
       - property def height(self): to retrieve it
       - property setter def height(self, value): to set it:
              - height must be an integer, otherwise raise a TypeError
                exception with the message height must be an integer
              - if height is less than 0, raise a ValueError exception with the
                message height must be >= 0
 3. Instantiation with optional width and height: def __init__(self, width=0,
    height=0):
"""


class Rectangle:
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        """intializes the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the values of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
