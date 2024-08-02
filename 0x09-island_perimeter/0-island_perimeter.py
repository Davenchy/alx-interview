#!/usr/bin/python3
""" Island Perimeter Interview Problem Solving """

WATER = 0
LAND = 1


def get_cell_state(grid: list[list[int]], r: int, c: int):
    """ Returns cell state, 0 for water and 1 for a land.
    if cell out of range will return 0 (water)

    Examples:
        >>> get_cell_state([[1]], 0, 0)
        1

        >>> get_cell_state([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 1, 1)
        1

        >>> get_cell_state([[]], 1, 1)
        0

        >>> get_cell_state([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 1, 1)
        0
    """
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
        return WATER
    return grid[r][c]


def count_land_water_sides(grid: list[list[int]], r: int, c: int) -> int:
    """ Count land sides that touches the water for a land cell at r, c

    Examples:
        >>> count_land_water_sides([[1]], 0, 0)
        4

        >>> count_land_water_sides([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 1, 1)
        4

        >>> count_land_water_sides([[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
        ... 1, 1)
        3"""
    sides_count = 0

    # make sure it is a land
    if get_cell_state(grid, r, c) != LAND:
        return 0

    # check sides
    for r, c in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:
        if get_cell_state(grid, r, c) == WATER:
            sides_count += 1

    return sides_count


def island_perimeter(grid: list[list[int]]):
    """ Returns the perimeter of the island described in grid
    For each grid cell value, 0 means water and 1 means land. each cell is
    a square with a side of 1 length unit.
    Cells only connected horizontally or vertically to form an island.
    Grid is rectangle and its width and height don't exceed 100 """

    perimeter = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                perimeter += count_land_water_sides(grid, r, c)
    return perimeter
