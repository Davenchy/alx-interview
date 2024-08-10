#!/usr/bin/python3
""" Solving prime game problem. """


def generate_primes(n):
    """ Generate all primes up to n. """
    primes = []

    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)
    return primes


def is_maria_wins(n, primes=None):
    """ Check if maria wins a game of n. """
    if primes is None:
        primes = generate_primes(n)

    counter = 0
    for i in primes:
        if i > n:
            break
        counter += 1
    return counter % 2 != 0


def isWinner(x, nums):
    """ Maria and Ben are playing a game.
    Given a set of consecutive integers starting from `1` up to and including
    `n`, they take turns choosing a prime number from the set and removing that
    number and its multiples from the set.
    The player that cannot make a move loses the game.

    They play x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is.

    Returns the player who won the most games or None if there is a tie."""
    maria_score, ben_score = 0, 0
    primes = generate_primes(max(nums[:x]))

    for i in range(x):
        n = nums[i]

        if is_maria_wins(n, primes):
            maria_score += 1
        else:
            ben_score += 1

    if maria_score > ben_score:
        return "Maria"
    if maria_score < ben_score:
        return "Ben"
    return None
