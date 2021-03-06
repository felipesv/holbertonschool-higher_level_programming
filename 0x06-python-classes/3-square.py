#!/usr/bin/python3
class Square:
    """ Square Object """

    def __init__(self, size=0):
        """ Constructor

        Note:
            create a square

        Arg:
            self: object that is being create
            size (int): size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    def area(self):
        """ Area

        Note:
            consult the square's area

        Arg:
            self: object that is being create
        """
        return self._Square__size**2
