#!/usr/bin/python3
'''
This module contains a function that will check if a given data set is a valid
utf-8 encoding
'''
from typing import List


def validUTF8(data: List) -> bool:
    '''
    This function will check if a given data set is a valid utf-8 encoding

    Args:
        data: List of integers

    Returns:
        True if the data is a valid utf-8 encoding
        False if the data is not a valid utf-8 encoding
    '''
    def check(num: int) -> int:
        '''
        This function will check if the given number is a valid utf-8 encoding

        Args:
            num: Integer

        Returns:
            Number of bytes in the utf-8 encoding
        '''
        masking = 1 << (8 - 1)
        index = 0
        while num & masking:
            masking >>= 1
            index += 1
        return index

    index = 0
    while index < len(data):
        j_index = check(data[index])
        k_index = index + j_index - (j_index != 0)
        index += 1
        if j_index == 1 or j_index > 4 or k_index >= len(data):
            return False
        while index < len(data) and index <= k_index:
            currently = check(data[index])
            if currently != 1:
                return False
            index += 1
    return True


if __name__ == "__main__":
    validUTF8 = __import__('0-validate_utf8').validUTF8

    all_data = [65]
    print(validUTF8(all_data))  # True

    all_data = [80, 121, 116, 104, 111, 110, 32,
                105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(all_data))  # True

    all_data = [229, 65, 127, 256]
    print(validUTF8(all_data))  # False
    all_data = []
    print(validUTF8(all_data))  # False
