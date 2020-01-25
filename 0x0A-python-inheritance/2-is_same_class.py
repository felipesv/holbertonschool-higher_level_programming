#!/usr/bin/python3
"""
returns True if the object is exactly an instance
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance
    """
    _type = type(obj)
    if _type == a_class:
        return True
    return False
