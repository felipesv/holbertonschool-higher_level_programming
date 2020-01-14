#!/usr/bin/python3
"""
Class to create a rectangle
"""


class Rectangle:
    """
    Class to create a rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        constructor
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        get the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        get the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        get the area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        get the parimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        get the rectangle stirng format
        """
        rest = ""
        if self.__width != 0 and self.__height != 0:
            rest = ""
            for i in range(self.__height):
                rest += "#" * self.__width
                rest += "\n"

        return rest

    def __repr__(self):
        """
        return the string to create it self
        """
        return 'Rectangle(width=' + str(self.__width) \
            + ', height=' + str(self.__height) + ')'

    def __del__(self):
        """
        msg to display when a instance is deleted
        """
        print("Bye rectangle...")
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
