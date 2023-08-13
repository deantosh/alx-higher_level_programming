#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:

        l = len(row) - 1
        j = 0

        for i in row:
            if j == l:
                print('{}'.format(i), end='')
            else:
                print('{}'.format(i), end=' ')
            j = j + 1
        print()
