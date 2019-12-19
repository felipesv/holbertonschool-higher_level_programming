#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [i[:] for i in matrix]
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            new_matrix[i][j] = matrix[i][j] * matrix[i][j]
    return new_matrix
