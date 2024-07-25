#!/usr/bin/python3

'''
This is a program to find the minimum number of coins needed to make a total
amount.
'''


def makeChange(deno_sorted, total_amount):
    '''
    This function takes in a list of denominations and a total amount and
    returns the minimum number of coins needed to make the total amount.
    If the total amount can't be made with the given denominations, the
    function returns -1.
    args:
        deno: list of integers
        total: integer
    return:
        integer
    '''
    if total_amount <= 0:
        return 0

    answer = []
    length = len(deno_sorted)
    deno_sorted = sorted(deno_sorted)
    index = length - 1
    while (index >= 0):
        while (total_amount >= deno_sorted[index]):
            total_amount -= deno_sorted[index]
            answer.append(deno_sorted[index])
        index -= 1
    if total_amount != 0:
        return -1
    return len(answer) if answer else -1


if __name__ == '__main__':

    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
