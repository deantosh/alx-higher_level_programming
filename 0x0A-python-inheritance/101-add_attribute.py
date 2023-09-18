#!/usr/bin/python3
"""defines: an add attribute function to object"""


def add_attribute(obj, attr, value):
    """Adds attribute to object

       raise TypeError:
             if can't add new attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
