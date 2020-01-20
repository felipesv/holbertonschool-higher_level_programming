#!/usr/bin/python3
"""
BaseGeometry
"""


class BaseGeometry:
    """
    BaseGeometry
    """

    def __init__(self):
        """
        empty constructor
        """
        pass

    def area(self):
        """
        generate a exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate values
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
