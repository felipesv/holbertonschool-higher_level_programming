#!/usr/bin/python3}
"""
reads and print n lines of a text file
"""


def read_lines(filename="", nb_lines=0):
    """
    reads and print n lines of a text file
    """
    if nb_lines <= 0:
        with open(filename, encoding="utf-8") as file:
            print(file.read())
    else:
        with open(filename, encoding="utf-8") as file:
            cnt = 0
            while (cnt < nb_lines):
                text = file.readline()
                print(text, end="")
                cnt += 1
