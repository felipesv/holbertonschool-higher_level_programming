#!/usr/bin/python3
"""
class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square
    """

    def __init__(self, size):
        """
        constructor
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        area
        """
        return self.__size ** 2

    def __str__(self):
        """
        get the size
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
