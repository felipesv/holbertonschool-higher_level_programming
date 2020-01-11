#!/usr/bin/python3
"""
Function to add two number
a (int, float): number 1
b (int, float): number 2
"""


def add_integer(a, b=98):
    """
    Function to add two number
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
