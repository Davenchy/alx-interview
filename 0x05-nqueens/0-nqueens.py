#!/usr/bin/python3
""" Solving N queens problem """

import sys
from typing import Generator, List


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
    if len(sol) <= 1:
        return True

    # valid solution does not have repeated values
    # or more than queen on the same column
    if len(set(sol)) != len(sol):
        return False

    # check diagonals
    for i in range(len(sol) - 1):
        if sol[i] == -1:
            return True
        for j in range(i + 1, len(sol)):
            a, b = sol[i], sol[j]
            delta = abs(a - b)
            if delta in (0, j - i):
                return False
    return True


def queens(sol: List[int], n: int):
    if len(sol) < n:
        cases = [i
                 for i in range(n)
                 if len(sol) == 0 or abs(sol[-1] - i) not in (0, 1)]
        for i in cases:
            queens(sol + [i], n)
    elif len(sol) == n:
        if is_solution(sol):
            print([[i, j] for i, j in enumerate(sol)])


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
