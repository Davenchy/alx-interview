#!/usr/bin/python3
"""
Rotate 2D Matrix Problem Solution
"""

from typing import List, Tuple


def next_cell(r, c, size) -> Tuple[int, int]:
    """ Get the next cell of swap for the current cell usint its (row, col)
    """
    return c, size - r - 1


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """ Rotate matrix 90 degrees clockwise in-place
    """
    size = len(matrix)

    for i in range(round(size / 2)):
        for j in range(size - 1 - i * 2):
            nxt, value = (i, j + i), matrix[i][j + i]

            for _ in range(5):
                r, c = nxt
                tmp = matrix[r][c]
                matrix[r][c] = value
                value = tmp
                nxt = next_cell(r, c, size)
