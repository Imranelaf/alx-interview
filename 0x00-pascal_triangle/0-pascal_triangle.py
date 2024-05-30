#!/usr/bin/python3

'''
This module contains a function that returns a list of lists that represents
the Pascal's Triangle of a given integer n.
'''


def pascal_triangle(n):
    '''
    This function takes in an integer n and returns a list of lists
    that represents the Pascal's Triangle of the given integer n.
    '''
    if n <= 0:
        return []
    ps = [[1]]
    for row_n in range(1, n):
        r = [1]
        for j in range(1, row_n):
            element = ps[row_n - 1][j - 1] + ps[row_n - 1][j]
            r.append(element)
        r.append(1)
        ps.append(r)

    return ps
