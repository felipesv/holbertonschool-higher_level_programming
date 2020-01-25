#!/usr/bin/python3
"""
is an instance of, or from class inherited
"""


def inherits_from(obj, a_class):
    _type1 = not (type(obj) is a_class)
    _type2 = isinstance(obj, a_class)
    return _type1 and _type2
