#!/usr/bin/python3
'''
This module contains a function that determines the winner of a game
'''


def generatePrimeNumbers(limit):
    '''
    Generate prime numbers up to a given limit
    Args:
        limit: integer representing the upper limit
    Returns:
        list: list of prime numbers
    '''
    prime_nums = []
    si_list = [True] * (limit + 1)
    for maybe_prime_num in range(2, limit + 1):
        if si_list[maybe_prime_num]:
            prime_nums.append(maybe_prime_num)
            for multiple in range(maybe_prime_num, limit + 1, maybe_prime_num):
                si_list[multiple] = False
    return prime_nums


def isWinner(numRounds, roundValues):
    '''
    Determine the winner of the game
    Args:
        numRounds: number of rounds played
        roundValues: list of integers representing the values of each round
    Returns:
        string: the winner of the game
    '''
    if not numRounds or not roundValues:
        return None
    maria_sc = ben_sc = 0
    for i in range(numRounds):
        prime_nums = generatePrimeNumbers(roundValues[i])
        if len(prime_nums) % 2 == 0:
            ben_sc += 1
        else:
            maria_sc += 1
    if maria_sc > ben_sc:
        return "Maria"
    elif ben_sc > maria_sc:
        return "Ben"
    return None
