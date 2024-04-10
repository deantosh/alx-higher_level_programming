#!/usr/bin/python
"""
divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """returns: new matrix"""

    # validate inputs
    validate_inputs(matrix, div)

    new_matrix = []
    for row in matrix:
        new_row = []
        for e in row:
            e = round((e / div), 2)
            new_row.append(e)
        new_matrix.append(new_row)
    return new_matrix


def validate_inputs(matrix, div):
    """validates matrix and the div"""

    # check if matrix is a list of lists
    matrix_rows = [isinstance(row, list) for row in matrix]
    if not isinstance(matrix, list) or not all(matrix_rows):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # checks if the matrix elements are int/floats
    elems = [isinstance(elem, (int, float)) for row in matrix for elem in row]
    if not all(elems):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # checks if the rows are of same size
    size = len(matrix[0])
    if not all(len(row) == size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # validates the div argument
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
