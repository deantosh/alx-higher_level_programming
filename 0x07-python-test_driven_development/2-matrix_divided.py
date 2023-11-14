#!/usr/bin/python3
"""Module defines  a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """return:
          a new matrix whose values are divided
    """
    if not isinstance(matrix, list) and \
       all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 2:
        len_1 = len(matrix[0])
        len_2 = len(matrix[1])

        if len_1 != len_2:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # create row and matrix
    new_matrix = []

    for row in matrix:
        new_row = []
        for ele in row:
            val = round((ele / div), 2)
            new_row.append(val)
        new_matrix.append(new_row)

    return new_matrix
