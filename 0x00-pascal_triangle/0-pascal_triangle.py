#!/usr/bin/python3


def pascal_triangle(n):
    '''
    This function takes in an integer n and returns a list of lists
    that represents the Pascal's Triangle of the given integer n.
    '''
    if n <= 0:
        return []
    triangle = [[1]]
    for row_n in range(1, n):
        row = [1]
        for j in range(1, row_n):
            element = triangle[row_n - 1][j - 1] + triangle[row_n - 1][j]
            row.append(element)
        row.append(1)
        triangle.append(row)

    return triangle
