#!/usr/bin/python3
"""Solution of minOperations problem"""


def find_divider(x: int) -> int:
    """find the nearest lower number of x that is divisible by x"""
    if x <= 3:
        return 1

    for i in range(x - 1, 1, -1):
        if x % i == 0:
            return i
    return 1


def minOperations(n: int) -> int:
    """find the minimum copyAll and paste operations to repeat the character
    n times.

    Examples:
        # copyAll > paste > copyAll > paste
        >>> minOperations(4)
        4

        # copyAll > paste > paste > copyAll > paste > paste
        >>> minOperations(9)
        6

        # copyAll > paste > paste > copyAll > paste > copyAll > paste
        >>> minOperations(12)
        7
        """
    if n <= 1:
        return 0
    elif n <= 5:
        return n

    x = find_divider(n)
    return (n // x) + minOperations(x)
