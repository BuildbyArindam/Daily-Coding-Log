"""
Problem   : Trace Path
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/trace-path3840/1
Difficulty: Easy
Topics    : Matrix
Date      : 2026-10-24

Approach:
    The starting cell can be chosen freely, so the path fits in the n x m grid
    if and only if its bounding box (the range of horizontal and vertical
    displacement from the start) fits inside the grid. Track the running
    position, minimum and maximum for each axis as [pos, min, max]. If
    (max - min) reaches m on columns or n on rows, the path must leave the
    grid, so return False. Otherwise, return True.

Time Complexity : O(|s|), a single pass over the path
Space Complexity: O(1)
"""


# ---------------------------------------------- Solution ---------------------------------------------------------------


class Solution:
    def isPossible(self, n: int, m: int, s: str) -> bool:
        # code here
        col = [0, 0, 0]
        row = [0, 0, 0]
        moves = {
            'L': (col, -1),
            'R': (col, 1),
            'D': (row, -1),
            'U': (row, 1),
        }
        for ch in s:
            axis, step = moves[ch]
            axis[0] += step
            if axis[0] < axis[1]:
                axis[1] = axis[0]
            elif axis[0] > axis[2]:
                axis[2] = axis[0]
            if col[2] - col[1] >= m or row[2] - row[1] >= n:
                return False
        return (col[2] - col[1] < m) and (row[2] - row[1] < n)
