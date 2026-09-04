"""
Problem: Cell Signal
Platform: FreeCodeCamp - Daily Coding Challenge (07-25)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-25
Date Solved: 2026-09-04
Difficulty: Easy-Medium
Topics: Arrays, Matrix, Simulation, Distance Calculation (Chebyshev/king-move distance), Brute Force

Approach:
Collect all towers (cells with value > 0) from the grid, each storing
its (row, col, required_distance). For every cell in the grid, check
whether its Chebyshev distance (max(|dr|, |dc|)) to each tower exactly
matches that tower's stored distance value. Return the first cell that
satisfies all towers simultaneously.

Time Complexity: O(R * C * T) — R,C = grid dimensions, T = number of towers
Space Complexity: O(T) — storage for the tower list
"""


# --------------------------- Solution --------------------------------


def find_signal(grid):
    towers = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] > 0:
                towers.append((r, c, grid[r][c]))
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            correct = True
            for tr, tc, distance in towers:
                actual_distance = max(abs(r - tr), abs(c - tc))
                if actual_distance != distance:
                    correct = False
                    break
            if correct:
                return [r, c]
