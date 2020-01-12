#!/usr/bin/python3
"""
Divides all elements of a matrix.
matrix: matrix
div: number to divide
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    """
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix \
            (list of lists) of integers/floats")

    for i in matrix:
        if type(i) != list:
            raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")

    for i in matrix:
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix \
                    (list of lists) of integers/floats")

    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise TypeError("division by zero")

    _matrix = [i[:] for i in matrix]
    for i in range(len(_matrix)):
        for j in range(len(_matrix[i])):
            _matrix[i][j] = round(_matrix[i][j]/div, 2)

    return _matrix
