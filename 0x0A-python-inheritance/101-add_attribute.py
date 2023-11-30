#!/usr/bin/python3
"""Module:
        defines a function thats adds a new attribute to an object
        raise a type error if object can't have new attributes.
"""


def add_attribute(obj, name, value):
    """Adds an attribute to an obhject"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
