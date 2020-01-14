#!/usr/bin/python3
"""
Class to create a rectangle
"""


class Rectangle:
    """
    Class to create a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

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
                rest += str(self.print_symbol) * self.__width
                if i + 1 != self.__height:
                    rest += "\n"

        return rest

    def __repr__(self):
        """
        return the string to create it self
        """
        return 'Rectangle(' + str(self.__width) \
            + ', ' + str(self.__height) + ')'

    def __del__(self):
        """
        msg to display when a instance is deleted
        """
        print("Bye rectangle...")
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """
        biggest rectangle
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 > area_2 or area_1 == area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        create a new instance object
        """
        new_obj = cls(size, size)
        return new_obj
