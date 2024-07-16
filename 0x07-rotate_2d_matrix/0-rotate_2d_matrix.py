#!/usr/bin/python3

'''
This module contains the implementation of the bolbol algorithm
'''


def rotate_2d_matrix(matrix):
    '''
    This function rotates a 2D matrix by 90 degrees

    Args:
        mat: a 2D matrix
    Returns:
        None
    '''
    size = len(matrix)
    for i in range(0, int(size / 2)):
        for j in range(i, size-i-1):
            temporary = matrix[i][j]
            matrix[i][j] = matrix[size-1-j][i]
            matrix[size-1-j][i] = matrix[size-1-i][size-1-j]
            matrix[size-1-i][size-1-j] = matrix[j][size-1-i]
            matrix[j][size-1-i] = temporary
