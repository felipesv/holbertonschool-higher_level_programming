#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    pascal = [[1]]
    new_list = []

    for i in range(n - 1):
        new_list.append(1)
        for j in range(len(pascal[i]) - 1):
            num_a = pascal[i][j]
            num_b = pascal[i][j + 1]
            new_list.append(num_a + num_b)
        new_list.append(1)
        pascal.append(new_list)
        new_list = []
    return pascal
