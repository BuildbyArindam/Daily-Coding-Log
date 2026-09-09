"""
Problem: Landing Spot
Platform: FreeCodeCamp - Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-07
Date Solved: 2026-09-09
Difficulty: Easy-Medium (matrix/grid scan problems like this are usually rated Easy on most platforms, Medium if adjacency-sum logic is unfamiliar)
Topics: Arrays, Matrix/Grid Traversal, Brute Force Search

Approach:
Scan every cell in the matrix. For each cell with value 0 (a valid
landing spot), sum the values of its up/down/left/right neighbors
(skipping out-of-bounds sides) to get a "danger" score. Track the
minimum danger score seen and its coordinates.

Time Complexity: O(rows * cols) - each cell visited once, each with
                  at most 4 neighbor lookups (O(1) each).
Space Complexity: O(1) extra space (excluding input matrix).
"""


# ---------------------- Solution ----------------------------


def find_landing_spot(matrix):
    safest_spot = None
    lowest_danger = float("inf")
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                danger = 0
                if row > 0:
                    danger += matrix[row - 1][col]
                if row < rows - 1:
                    danger += matrix[row + 1][col]
                if col > 0:
                    danger += matrix[row][col - 1]
                if col < cols - 1:
                    danger += matrix[row][col + 1]
                if danger < lowest_danger:
                    lowest_danger = danger
                    safest_spot = [row, col]
    return safest_spot
