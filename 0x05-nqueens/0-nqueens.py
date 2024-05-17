#!/usr/bin/python3
""" Solving N queens problem """

import sys
from typing import List


def is_solution(sol: List[int]) -> bool:
    """ check if solution is valid
    Examples:
        >>> is_solution([])
        True
        >>> is_solution([1, 2])
        False
        >>> is_solution([1, 3])
        True
        >>> is_solution([1, 1])
        False
        >>> is_solution([1, 4, 2])
        True
        >>> is_solution([1, 3, 6, 4])
        False
        >>> is_solution([1, 2, 3, 4])
        False
        >>> is_solution([1, 2, 3, 3])
        False
        >>> is_solution([1, 3, 0, 2])
        True
        >>> is_solution([2, 0, 3, 1])
        True
    """
    qn = len(sol)
    # no repeats on the same column
    if len(set(sol)) != qn:
        return False

    # calculate diagonals
    pos, neg = set(), set()
    for i in range(qn):
        pos.add(i + sol[i])
        neg.add(i - sol[i])

    # no repeats on diagonals
    return len(pos) == len(neg) == qn


def queens(sol: List[int], n: int):
    is_sol = is_solution(sol)
    if not is_sol:
        return
    if is_sol and len(sol) == n:
        print([[i, j] for i, j in enumerate(sol)])
        return

    if len(sol) < n:
        cases = [i
                 for i in range(n)
                 if len(sol) == 0 or abs(sol[-1] - i) not in (0, 1)]
        for i in cases:
            queens(sol + [i], n)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print('N must be at least 4')
            sys.exit(1)
        queens([], n)
    except ValueError:
        print('N must be a number')
