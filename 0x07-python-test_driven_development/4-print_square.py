#!/usr/bin/python3
"""
prints a square with the character #
size: size of square
"""


def print_square(size):
    """
    prints a square with the character #
    """
    if type(size) != int and type(size) != float:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(int(size)):
        for i in range(int(size)):
            print("#", end="")
        print("")
