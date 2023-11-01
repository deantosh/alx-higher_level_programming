#!/usr/bin/python3
"""defines a locked class"""


class LockedClass:
    """
        Only allows the creation of first_name attribute
    """
    __slots__ = ["first_name"]
