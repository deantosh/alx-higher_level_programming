#!/usr/bin/python3
"""
Script contains a class ``LockedClass`` with no class or object attribute, that
prevents the user from dynamically creating new instance attributes, except if
the new instance attribute is called first_name.
"""


class LockedClass:
    """defines a locked class"""

    __slots__ = ("first_name",)
