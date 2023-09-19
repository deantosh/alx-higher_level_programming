#!/usr/bin/python3
"""defines: Base class"""


class Base():
    """defines a base class for all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
