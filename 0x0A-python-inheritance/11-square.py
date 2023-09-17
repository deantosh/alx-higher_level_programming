#!/usr/bin/python3
"""Module: defines class - Square
           that inherits from a subclass rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a square"""

    def __init__(self, size):
        """initializes the square"""

        """validate the value of size attribute"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
