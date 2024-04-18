#!/usr/bin/python3
"""
Module defines a ``Rectangle`` class that is a subclass of ``Base`` class.

Requirements:
 - In the file models/rectangle.py
 - Class Rectangle inherits from Base
 - Private instance attributes, each with its own public getter and setter:
        __width -> width
        __height -> height
        __x -> x
        __y -> y
 - Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
 - Call the super class with id - this super call with use the logic of the
   __init__ of the Base class
 - Assign each argument width, height, x and y to the right attribute
"""
from models.base import Base


class Rectangle(Base):
    """defines a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the class"""

        # call __init__ method from the base class
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # setter and getter methods for instance attributes
    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width value"""
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height value"""
        self.__height = value

    @property
    def x(self):
        """retrieves x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x value"""
        self.__x = value

    @property
    def y(self):
        """retrieves y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y value"""
        self.__y = value
