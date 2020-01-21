#!/usr/bin/python3
"""
number of lines
"""


def number_of_lines(filename=""):
    """
    number of lines
    """
    with open(filename, encoding="utf-8") as file:
        return len(file.read().split("\n"))
