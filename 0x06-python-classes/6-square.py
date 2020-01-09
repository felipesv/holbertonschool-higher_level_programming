#!/usr/bin/python3
class Square:
    """ Square Object """

    def __init__(self, size=0, position=(0, 0)):
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
            self._Square__position = position

        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._Square__position = position

    def area(self):
        """ Area

        Note:
            consult the square's area

        Arg:
            self: object that is being create
        """
        return self._Square__size**2

    @property
    def size(self):
        """ get the size of the square

        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """ set the size of the square
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

    def my_print(self):
        """ orint the square
        """
        i = 0
        for k in range(self._Square__position[1]):
            print("")

        for i in range(self._Square__size):
            for k in range(self._Square__position[0]):
                print(" ", end="")
            for j in range(self._Square__size):
                print("#", end="")
            print("")
        if i == 0:
            print("")

    @property
    def position(self):
        """ get the position of the square

        """
        return self._Square__position

    @position.setter
    def position(self, value):
        """ set the position of the square
        """
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._Square__position = value
