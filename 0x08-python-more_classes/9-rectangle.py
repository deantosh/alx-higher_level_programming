#!/usr/bin/python3
"""
This module defines a ``rectangle`` class.

Requirements:
 1. Private instance attribute: width:
       - property def width(self): to retrieve it
       - property setter def width(self, value): to set it:
              - width must be an integer, otherwise raise a TypeError exception
                with the message width must be an integer
              - if width is less than 0, raise a ValueError exception with the
                message width must be >= 0
 2. Private instance attribute: height:
       - property def height(self): to retrieve it
       - property setter def height(self, value): to set it:
              - height must be an integer, otherwise raise a TypeError
                exception with the message height must be an integer
              - if height is less than 0, raise a ValueError exception with the
                message height must be >= 0
 3. Instantiation with optional width and height: def __init__(self, width=0,
    height=0):
 4. Public instance method: def area(self): that returns the rectangle area
 5. Public instance method: def perimeter(self): that returns the rectangle
    perimeter:
      - if width or height is equal to 0, perimeter has to be equal to 0
 6. print() and str() should print the rectangle with the character(s) stored
    in print_symbol:
      - if width or height is equal to 0, return an empty string
 7. repr() should return a string representation of the rectangle to be able to
    recreate a new instance by using eval()
 8. Print the message Bye rectangle... (... being 3 dots not ellipsis) when an
    instance of Rectangle is deleted
 9. Public class attribute number_of_instances:
      - Initialized to 0
      - Incremented during each new instance instantiation
      - Decremented during each instance deletion
 10. Public class attribute print_symbol:
       - Initialized to #
       - Used as symbol for string representation
       - Can be any type
 11. Static method def bigger_or_equal(rect_1, rect_2): that returns the
     biggest rectangle based on the area;
        - rect_1 must be an instance of Rectangle, otherwise raise a TypeError
          exception with the message rect_1 must be an instance of Rectangle
        - rect_2 must be an instance of Rectangle, otherwise raise a TypeError
          exception with the message rect_2 must be an instance of Rectangle
        - Returns rect_1 if both have the same area value
 12. Class method def square(cls, size=0): that returns a new Rectangle
     instance with width == height == size
"""


class Rectangle:
    """defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """intializes the class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the values of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """defines area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """defines the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints the rectangle"""
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect
        for h in range(self.__height):
            for w in range(self.__width):
                rect += str(self.print_symbol)
            if h < (self.__height - 1):
                rect += "\n"
        return rect

    def __repr__(self):
        """returns string representation of the object"""
        obj_str = "Rectangle({:d}, {:d})".format(self.__width, self.__height)
        return obj_str

    def __del__(self):
        """deletes an object"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle between the two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns an object with width=height=size"""
        return cls(size, size)
