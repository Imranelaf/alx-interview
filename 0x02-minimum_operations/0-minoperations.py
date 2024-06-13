#!/usr/bin/python3
'''This module contains the function minOperations'''


def minOperations(n):
    '''
    This function calculates the minimum operations to reach n
    '''
    if (n < 2):
        return 0
    operations, rt = 0, 2
    while rt <= n:
        if n % rt == 0:
            operations += rt
            n = n / rt
            rt -= 1
        rt += 1
    return operations
