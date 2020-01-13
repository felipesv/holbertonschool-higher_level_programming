#!/usr/bin/python3
"""
prints a text with 2 new lines after each charac . ? :
text: text to print

"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each charac . ? :
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    text = text.rstrip()
    _len = len(text)
    _cnt = 0

    while _cnt < _len and ord(text[_cnt]) == 32:
        _cnt += 1

    while _cnt < _len:
        if text[_cnt] == "." or text[_cnt] == "?" or text[_cnt] == ":":
            print("{:s}".format(text[_cnt]), end="\n\n")
            while (_cnt + 1) < _len and ord(text[_cnt + 1]) == 32:
                _cnt += 1
        else:
            print("{:s}".format(text[_cnt]), end="")

        _cnt += 1
