#!/usr/bin/python3
"""Module defines Rectangle class, that inherits from BaseGeometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Rectangle"""
    def __init__(self, width, height):
        """Validate values
              - Initialize the class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Defines the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return:
                  unofficial string representation of the object
        """
        obj_str = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return obj_str
