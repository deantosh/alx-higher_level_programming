#!/usr/bin/python3
"""Module: defines a class: Rectangle
           that inherits from base class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines Rectangle class"""

    def __init__(self, width, height):
        """initializes the class"""

        """Validate:
                    width - value
                    height - value
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def __str__(self):
        """returns: class description"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

    def area(self):
        """returns: area of a rectangle"""
        return self.__width * self.__height
