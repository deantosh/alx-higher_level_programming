#!/usr/bin/python3
"""Module defines a class Square that inherits from Rectangle class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines a square"""
    def __init__(self, size):
        """
           initialize class
        """
        self.__size = size
        super().__init__(self.__size, self.__size)
