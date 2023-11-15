#!/usr/bin/python3
"""Module checks to see if an object is an instance
   of both child/parent class
"""


def is_kind_of_class(obj, a_class):
    """return:
              True if instance
              False if not
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
