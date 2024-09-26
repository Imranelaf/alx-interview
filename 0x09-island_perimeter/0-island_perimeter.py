#!/usr/bin/python3
""" island perimeter """


def island_perimeter(grid):
    '''
    This function calculates the perimeter of an island
    Args:
        grid: list of list of integers
    Returns:
        perimeter: integer
    '''
    if not grid:
        return 0

    r, cs = len(grid), len(grid[0])
    per = 0

    for i in range(r):
        for j in range(cs):
            if grid[i][j] == 1:
                per += 4
                if i > 0 and grid[i - 1][j] == 1:
                    per -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    per -= 2

    return per


if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]

    print(island_perimeter(grid))

    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

    grid = []
    print(island_perimeter(grid))
    grid = [
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
    ]
    print(island_perimeter(grid))
