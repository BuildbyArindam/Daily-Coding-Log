"""
Problem   : Matrix Rotate
Platform  : FreeCodeCamp — Daily Coding Challenge
Link      : https://www.freecodecamp.org/learn/daily-coding-challenge/09-06
Date      : 2026-09-06
Difficulty: Easy-Medium
Topics    : Arrays, Matrix, In-place Rotation, Simulation

Approach:
    Rotate the matrix 90 degrees clockwise using the classic
    "reverse rows, then transpose" trick:
      1. matrix[::-1] reverses the row order (flips vertically).
      2. zip(*...) transposes the reversed matrix.
    This avoids manual index math and works for any N x N (and
    even non-square) input in one line.

Time Complexity : O(n*m)  — every cell is visited once during zip/transpose
Space Complexity: O(n*m)  — new matrix returned (zip + list comprehension)
"""


# ------------------------- Solution -----------------------------------


def rotate(matrix):
    return [list(row) for row in zip(*matrix[::-1])]
