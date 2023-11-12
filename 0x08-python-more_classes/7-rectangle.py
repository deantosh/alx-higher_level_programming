#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """defines rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes the data
           Args:
                width - width of the rectangle
                height - height of the rectangle
        """
        # validate values
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
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the width
           Args:
                width - width of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the height
           Args:
                height - height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """defines the perimeter of the rectangle"""
        if self.__width == 0 or self.height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))

    def area(self):
        """defines the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """returns: a string representation of the rectangle"""
        r_str = ""
        if self.__width == 0 or self.__height == 0:
            return r_str
        for i in range(self.__height):
            if i > 0:
                r_str += "\n"
            for j in range(self.__width):
                r_str += str(self.print_symbol)
        return r_str

    def __repr__(self):
        """returns: a string representation of the object code"""
        return f"{type(self).__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """deletes an instance of a class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
