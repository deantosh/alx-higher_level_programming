#!/usr/bin/python3
"""Module defines a pascal triangle
"""


def pascal_triangle(n):
    """returns:
               pascal triangle
    """
    # when n is equal or less than 0
    if n <= 0:
        return []

    # when n == 1
    triangle = [[1]]

    # when n > 1
    while len(triangle) != n:
        last_row = triangle[-1]
        tmp = [1]
        for i in range(len(last_row) - 1):
            tmp.append(last_row[i] + last_row[i + 1])
        tmp.append(1)
        triangle.append(tmp)

    return triangle
