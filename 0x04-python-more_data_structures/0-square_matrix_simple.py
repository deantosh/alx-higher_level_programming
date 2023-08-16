#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    #create a new matrix
    new_matrix = []

    for row in matrix:
        new_row = list(map(lambda i: i * i, row))
        new_matrix.append(new_row)

    return new_matrix
