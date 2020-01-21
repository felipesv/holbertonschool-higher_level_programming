#!/usr/bin/python3
"""
writes a string to a text file and returns the number
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file and returns the number
    """
    with open(filename, encoding="utf-8") as file:
        count = 0
        for line in file.readlines():
            count += 1 + len(line)
        return count
