#!/usr/bin/python3
"""
add attribute to obj class
"""


def add_attribute(cls, attr, value):
    """
    add attribute to obj class
    """
    if hasattr(cls, "__dict__")is False:
        raise TypeError("can't add new attribute")
    setattr(cls, attr, value)
