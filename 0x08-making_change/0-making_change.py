#!/usr/bin/python3
"""My solution for the problem 0x08-making_change."""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """This function will use any amount of coin value in `coins` to make
    change for `total`.

    Returns the minimum count of coins needed to make a change for `total` if
    possible otherwise returns -1.

    Examples:
        >>> makeChange([1, 2, 25], 36)
        7

        >>> makeChange([1256, 54, 48, 16, 102], 1453)
        -1
    """
    count = 0  # number of coins used
    remaining = total  # amount of change remaining

    # sort coins in decreasing order
    coins.sort(reverse=True)

    # loop through each coin
    for coin_value in coins:
        # calculate number of coins can be used using this coin
        count += remaining // coin_value
        # subtract from remaining the value of the coin * used_count
        remaining %= coin_value
        # if remaining == 0 then we have found the count of coins needed
        if remaining == 0:
            return count

    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
