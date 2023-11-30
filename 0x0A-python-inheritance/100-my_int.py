#!/usr/bin/python3
"""Module defines a rebel class MyInt that inherits from int"""


class MyInt(int):
    """defines int class"""
    def __eq__(self, value):
        """Override == operator with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior"""
        return self.real == value
