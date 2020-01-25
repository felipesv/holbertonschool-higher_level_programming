#!/usr/bin/python3
"""
class MyInt
"""


class MyInt(int):
    """
    class MyInt
    """
    def __eq__(self, other):
        """
        == is the opposite
        """
        return not (self.numerator == other)

    def __ne__(self, other):
        """
        != is the opposite
        """
        return not (self.numerator != other)
