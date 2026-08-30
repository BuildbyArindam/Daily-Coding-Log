"""
Problem: Magic Square Solver
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-01
Date Solved: 2026-08-30

Approach:
Find the single zero (missing) cell in the 3x3 grid. Build all 8 lines
(3 rows, 3 cols, 2 diagonals). Use the lines that are fully filled to
determine the target magic sum. For each line containing the missing
cell, solve for the candidate value and check all such lines agree.
Fill in the candidate, then re-validate every line sums to the magic
sum before returning it (guards against multiple zeros/inconsistent
grids slipping through).

Time Complexity: O(1) — fixed 3x3 grid, constant number of lines/cells
Space Complexity: O(1) — fixed-size line list, no growth with input
"""


# ------------------------------- Solution -----------------------------------


def solve_magic_square(grid):
    zero_positions = []
    for r in range(3):
        for c in range(3):
            if grid[r][c] == 0:
                zero_positions.append((r, c))
    if len(zero_positions) != 1:
        return "impossible"
    missing_r, missing_c = zero_positions[0]
    lines = [
        grid[0], grid[1], grid[2],
        [grid[0][0], grid[1][0], grid[2][0]],
        [grid[0][1], grid[1][1], grid[2][1]],
        [grid[0][2], grid[1][2], grid[2][2]],
        [grid[0][0], grid[1][1], grid[2][2]],
        [grid[0][2], grid[1][1], grid[2][0]]
    ]
    complete_sums = [sum(line) for line in lines if 0 not in line]
    if not complete_sums:
        return "impossible"
    magic_sum = complete_sums[0]
    if any(s != magic_sum for s in complete_sums):
        return "impossible"
    candidate = None
    for line in lines:
        if 0 in line:
            value = magic_sum - sum(line)
            if candidate is None:
                candidate = value
            elif candidate != value:
                return "impossible"
    grid[missing_r][missing_c] = candidate
    for line in [
        grid[0], grid[1], grid[2],
        [grid[0][0], grid[1][0], grid[2][0]],
        [grid[0][1], grid[1][1], grid[2][1]],
        [grid[0][2], grid[1][2], grid[2][2]],
        [grid[0][0], grid[1][1], grid[2][2]],
        [grid[0][2], grid[1][1], grid[2][0]]
    ]:
        if sum(line) != magic_sum:
            grid[missing_r][missing_c] = 0
            return "impossible"
    grid[missing_r][missing_c] = 0
    return candidate
