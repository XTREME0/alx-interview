#!/usr/bin/python3
"""Island perimeter Task """


def island_perimeter(grid):
    """ Calc the perimeter of an island. """
    per = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for x, row in enumerate(grid):
        m = len(row)
        for y, cell in enumerate(row):
            if cell == 0:
                continue
            e = (
                x == 0 or (len(grid[x - 1]) > y and grid[x - 1][y] == 0),
                y == m - 1 or (m > y + 1 and row[y + 1] == 0),
                x == n - 1 or (len(grid[x + 1]) > y and grid[x + 1][y] == 0),
                y == 0 or row[y - 1] == 0,
            )
            per += sum(e)
    return per
