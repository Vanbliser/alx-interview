#!/usr/bin/python3
# pylint: disable=C0103


"""contains isliand_perimeter function
"""


def island_perimeter(grid):
    """A function to calculate the perimeter of the island described in grid.

    Args:
        grid (list): a list of lists of integers where 0 represents water
        and 1 represent land

    Returns:
        (int): the perimeter of the island described in grid
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
