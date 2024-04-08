#!/usr/bin/python3
"""
Pascal's Triangle interview question
"""


def generate_next_row(prev_row, length):
    """
    Generates the next row of the triangle

    Args:
        prev_row (list): The previous row
        length (int): The length of the previous row

    Returns:
        list: The next row
    """
    next_row = [1]
    if not length:
        return next_row

    for i in range(length - 1):
        next_row.append(prev_row[i] + prev_row[i + 1])
    next_row.append(1)

    return next_row


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n

    Args:
        n (int): The height of the triangle

    Examples:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

        >>> pascal_triangle(1)
        [[1]]

        >>> pascal_triangle(0)
        []
    """
    triangle = []

    for i in range(n):
        next_row = generate_next_row(triangle[i - 1] if i > 0 else [], i)
        triangle.append(next_row)

    return triangle
