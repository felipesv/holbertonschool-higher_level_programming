#!/usr/bin/python3}
"""
reads and print n lines of a text file
"""


def read_lines(filename="", nb_lines=0):
    """
    reads and print n lines of a text file
    """
    num_lines = len(open(filename).readlines())
    if nb_lines <= 0 or nb_lines >= num_lines:
        with open(filename, encoding="utf-8") as file:
            for line in file:
                print(line, end="")
    else:
        with open(filename, encoding="utf-8") as file:
            cnt = 0
            while (cnt < nb_lines):
                text = file.readline()
                print(text, end="")
                cnt += 1
