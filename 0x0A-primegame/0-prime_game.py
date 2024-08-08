#!/usr/bin/python3
""" Solving prime game problem. """

prime_memory = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def is_prime(n):
    """ Check if number is prime. """
    if n in prime_memory:
        return True
    if n <= 30:
        return False

    for i in range(2, n // 3):
        if n % i == 0:
            return False

    prime_memory.append(n)
    return True


def is_maria_wins(n):
    """ Check if maria wins a game of n. """
    primes = [i for i in range(n + 1) if is_prime(i)]
    return len(primes) % 2 != 0


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

    for i in range(x):
        n = nums[i]

        if is_maria_wins(n):
            maria_score += 1
        else:
            ben_score += 1

    if maria_score > ben_score:
        return "Maria"
    if maria_score < ben_score:
        return "Ben"
    return None
