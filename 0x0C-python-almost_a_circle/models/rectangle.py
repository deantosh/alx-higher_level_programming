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
 - Validate all the attributes setter methods:
    0. If the input is not an integer, raise the TypeError exception with the
       message: <name of the attribute> must be an integer. Example: width must
       be an integer
    1. If width or height is under or equals 0, raise the ValueError exception
       with the message: <name of the attribute> must be > 0. Example: width
       must be > 0
    2. If x or y is under 0, raise the ValueError exception with the message:
       <name of the attribute> must be >= 0. Example: x must be >= 0
 - Add public instance method ``area``, which return area of rectangle.
 - Add public method ``display``, that prints to stdout the Rectangle with
   character '#'.
 - Override the __str__ method so that it returns in the below format:
       -> [Rectangle] (<id>) <x>/<y> - <width>/<height>
"""
from models.base import Base


class Rectangle(Base):
    """defines a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the class"""

        # validate input
        Rectangle.validate_input("width", width)
        Rectangle.validate_input("height", height)
        Rectangle.validate_input("x", x)
        Rectangle.validate_input("y", y)

        # call __init__ method from the base class
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # setter and getter methods for instance attributes

    @staticmethod
    def validate_input(attr, value):
        """validates the inputs and raises TypeError if not correct format"""
        if not isinstance(value, int):
            raise TypeError(f"{attr} must be an integer")
        if (attr == 'width' or attr == 'height') and value <= 0:
            raise ValueError(f"{attr} must be > 0")
        if (attr == 'x' or attr == 'y') and value < 0:
            raise ValueError(f"{attr} must be >= 0")

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width value"""
        Rectangle.validate_input("width", value)
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height value"""
        Rectangle.validate_input("height", value)
        self.__height = value

    @property
    def x(self):
        """retrieves x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x value"""
        Rectangle.validate_input("x", value)
        self.__x = value

    @property
    def y(self):
        """retrieves y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y value"""
        Rectangle.validate_input("y", value)
        self.__y = value

    def area(self):
        """returns: area of a rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """prints the rectangle, take into account (x, y) attributes"""
        rect = ""
        if self.__y:
            for k in range(self.__y):
                rect += "\n"
        for i in range(self.__height):
            if self.__x:
                for l in range(self.__x):
                    rect += " "
            for j in range(self.__width):
                rect += "#"
            rect += "\n"
        print(rect, end="")

    def __str__(self):
        """returns an informal string representation of the object"""
        obj_str = f"[Rectangle] (\
{self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
        return obj_str
