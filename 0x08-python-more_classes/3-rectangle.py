#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """represents a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes the data
           Args:
                 width - width of the rectangle
                 height - height of the rectangle

           raise exception:
                 value is not an integer
                 value is not positive
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """gets the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the width
           Args:
                width - width of the rectangle

           raise Exceptions:
                value is not an integer
                value is not a positive
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height value"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the height attribute
           Args:
                height - height of the rectangle

           raise Exception:
                value is not an integer
                value is not positive
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def perimeter(self):
        """defines the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)

        return ((self.__width * 2) + (self.__height * 2))

    def area(self):
        """defines the area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self) -> str:
        """returns a string representation of rectangle"""
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return (rectangle)

        for row in range(self.__height):
            for column in range(self.__width):
                rectangle += "#"
            rectangle += "\n"
        return (rectangle)
