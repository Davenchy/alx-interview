#!/usr/bin/python3
"""Solution of minOperations problem"""


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

    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return n // i + minOperations(i)
    return n
