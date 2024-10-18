#!/usr/bin/python3
"""Contains isWinner(x, num) function"""


def isWinner(x, num):
    """A function that determines the winner of the Prime Game.

    Args:
        x (int): number of rounds
        num (list): an array of n

    Returns:
        string: name of the player that won the most rounds
                If the winner cannot be determined, return None
    """
    
    if not num or x < 1:
        return None

    max_num = max(num)

    primes = [True for _ in range(max(max_num + 1, 2))]

    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not primes[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            primes[j] = False

    primes[0] = primes[1] = False

    prime_count = 0
    for i in range(len(primes)):
        if primes[i]:
            prime_count += 1
        primes[i] = prime_count

    winner = 'Ben'
    player1_score = 0

    for i in num:
        player1_score += primes[i] % 2 == 1

    if player1_score * 2 == len(num):
        winner = None
    elif player1_score * 2 > len(num):
        winner = "Maria"

    return winner
