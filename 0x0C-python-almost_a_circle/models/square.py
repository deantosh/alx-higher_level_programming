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
 - Update the class Square by adding the public getter and setter size
       -> The setter should assign (in this order) the width and the height -
          with the same value
       -> The setter should have the same value validation as the Rectangle for
          width and height - No need to change the exception error message (It
          should be the one from width)
 - Update the class Square by adding the public method def update(self, *args,
   **kwargs) that assigns attributes:
       -> *args is the list of arguments - no-keyworded arguments
       -> 1st argument should be the id attribute
       -> 2nd argument should be the size attribute
       -> 3rd argument should be the x attribute
       -> 4th argument should be the y attribute
   - **kwargs can be thought of as a double pointer to a dictionary: key/value
     (keyworded arguments)
   - **kwargs must be skipped if *args exists and is not empty
   - Each key in this dictionary represents an attribute to the instance
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

    @property
    def size(self):
        """retrieves the size of the square"""
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """sets the value of the size of the square"""

        # validate value of size attribute
        self.validate_input("width", value)

        self._Rectangle__width = value
        self._Rectangle__height = value

    def update(self, *args, **kwargs):
        """update attribute values in square object"""
        if args:
            # handle args
            attr_list = ['id', 'size', 'x', 'y']
            num_args = len(args)

            # validate input
            for i in range(num_args):
                self.validate_input(attr_list[0], args[i])

            if num_args > 0:
                self.id = args[0]
            if num_args > 1:
                self._Rectangle__width = args[1]
                self._Rectangle__height = args[1]
            if num_args > 2:
                self._Rectangle__x = args[2]
            if num_args > 3:
                self._Rectangle__y = args[3]
        else:
            # handle kwargs
            for key, value in kwargs.items():
                if key not in kwargs:
                    continue
                setattr(self, key, value)
