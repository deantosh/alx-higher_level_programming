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
 4. Public instance method: def area(self): that returns the rectangle area
 5. Public instance method: def perimeter(self): that returns the rectangle
    perimeter:
      - if width or height is equal to 0, perimeter has to be equal to 0
 6. print() and str() should print the rectangle with the character #:
      - if width or height is equal to 0, return an empty string
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

    def area(self):
        """defines area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """defines the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints the rectangle"""
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect
        for h in range(self.__height):
            for w in range(self.__width):
                rect += "#"
            if h < (self.__height - 1):
                rect += "\n"
        return rect
