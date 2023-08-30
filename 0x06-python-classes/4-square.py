#!/usr/bin/python3
"""defines a square"""


class Square:
    """initializes the data"""
    def __init__(self, size=0):
        """raise an error"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """defines the current square are"""
    def area(self):
        """returns the square area"""
        return (self.__size * self.__size)

    """retrieves the value of size"""
    @property
    def size(self):
        return (self.__size)

    """sets the value of size"""
    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
