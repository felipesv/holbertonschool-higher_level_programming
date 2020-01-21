#!/usr/bin/python3
"""
writes a string to a text file and returns the number
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file and returns the number
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        count = file.write(text)
        return count
