#!/usr/bin/python3
"""
Module defines a class that inherits from ``Rectangle`` class.

Requirements:
 - Class Square inherits from Rectangle
 - Class constructor: def __init__(self, size, x=0, y=0, id=None)::
       -> Call the super class with id, x, y, width and height - this super
          call will use the logic of the __init__ of the Rectangle class. The
          width and height must be assigned to the value of size
       -> You must not create new attributes for this class, use all attributes
          of Rectangle - As reminder: a Square is a Rectangle with the same
          width and height
       -> All width, height, x and y validation must inherit from Rectangle -
          same behavior in case of wrong data
 - The overloading __str__ method should return [Square] (<id>) <x>/<y> -
   <size> in our case, width or height
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints informal string representation of Square class"""
        str = f"[Square]\
 ({self.id}) {self._Rectangle__x}/{self._Rectangle__y}\
 - {self._Rectangle__width}"
        return str
