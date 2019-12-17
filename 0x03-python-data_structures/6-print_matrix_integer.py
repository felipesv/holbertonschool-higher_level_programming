#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len_arr1 = len(matrix)
    len_arr2 = len(matrix[0])
    for i in range(0, len_arr1):
        for j in range(0, len_arr2):
            print("{:d}".format(matrix[i][j]), end="")
            if ((j + 1) != len_arr2):
                print("{:s}".format(" "), end="")
        print("{:s}".format("\n"), end="")
