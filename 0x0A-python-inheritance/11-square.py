#!/usr/bin/python3
"""Module defines a class Square that inherits from Rectangle class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines a square"""
    def __init__(self, size):
        """
           initialize class
        """
        Rectangle.integer_validator(self, "size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        obj_str = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return obj_str
