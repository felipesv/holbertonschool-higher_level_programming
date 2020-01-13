#!/usr/bin/python3
"""
multiply two matrices
m_a: matrix 1
m_b: matrix 2
"""


def matrix_mul(m_a, m_b):
    """
    multiply two matrices
    """
    row_ma = 0
    col_ma = 0
    row_mb = 0
    col_mb = 0

    if type(m_a) != list:
        raise TypeError("m_a must be a list")

    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    for i in m_a:
        if type(i) != list:
            raise TypeError("m_a must be a list of lists")

    for i in m_b:
        if type(i) != list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for i in m_a:
        if len(i) == 0:
            raise ValueError("m_a can't be empty")

    for i in m_b:
        if len(i) == 0:
            raise ValueError("m_b can't be empty")

    for i in m_a:
        row_ma += 1
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("m_a should contain only integers or floats")

    for i in m_b:
        row_mb += 1
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("m_b should contain only integers or floats")

    for i in m_a:
        if len(i) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for i in m_b:
        if len(i) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    col_ma = len(m_a[0])
    col_mb = len(m_b[0])

    if col_ma != row_mb:
        raise ValueError("m_a and m_b can't be multiplied")

    col_a = 0
    row_a = 0

    col_b = 0
    row_b = 0

    valor = 0
    _matriz = []

    while row_a < row_ma:
        sub_mat = []
        while col_b < col_mb:
            while row_b < row_mb:
                valor += m_a[row_a][col_a] * m_b[row_b][col_b]
                row_b += 1
                col_a += 1
            sub_mat.append(valor)

            col_a = 0
            col_b += 1
            row_b = 0
            valor = 0
        _matriz.append(sub_mat)
        row_a += 1
        col_b = 0

    return _matriz
