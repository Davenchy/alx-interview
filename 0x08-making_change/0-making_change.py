#!/usr/bin/python3
""" Making Change Interview Challenge Solution """


from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """ determine the fewest number of coins needed to meet a given amount total

    Args:
        coins: list of positive integers representing the values of each coin
        total: total amount to be measured

    Returns 0 if total is 0 or less.

    Returns -1 if total can't be met by any combination of coins.

    Returns the fewest number of coins needed to meet the total
    if total can be met by a combination of coins. """
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    counter = 0

    for coin in sorted_coins:
        while total >= coin:
            count = total // coin
            counter += count
            total -= count * coin

        if total <= 0:
            break

    return counter if total == 0 else -1
