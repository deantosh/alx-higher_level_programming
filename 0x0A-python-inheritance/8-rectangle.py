#!/usr/bin/python3
"""
Module defines a class ``Rectangle``, which inherits from ``BaseGeometry``
class defined in 7-base_geometry.py module.

Class is implemented with:

 - Instantiation with width and height: def __init__(self, width, height):
 - width and height must be private. No getter or setter
 - width and height must be positive integers, validated by integer_validator
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """defines a rectangle"""
    def __init__(self, width, height):
        """initializes the class"""

        # validate the input
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
