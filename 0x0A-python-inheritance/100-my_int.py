#!/usr/bin/python3
"""defines :a derived class MyInt that inherits
           from baseclass int
"""


class MyInt(int):
    """defines MyInt class"""

    def __eq__(self, value):
        """override: equal to comparison
                    changes from == to !=
        """
        return self.real != value

    def __ne__(self, value):
        """override: not equal to comparison
                    changes from != to ==
        """
        return self.real == value
