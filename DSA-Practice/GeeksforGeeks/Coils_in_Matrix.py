"""
Problem   : Coils in Matrix
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/form-coils-in-a-matrix4726/1
Difficulty: Medium
Topics    : Matrix
Date      : 2026-10-03

Approach:
    The 4n x 4n matrix (filled row-wise with 1..16n^2) is never built.
    Any cell's value is computed directly as r * m + c + 1. Each coil is
    traced as a layered spiral: walk one boundary strip (down, across, up,
    back), then shrink the bounding box by 2 on every side and repeat,
    since a coil winds with a gap of one row/column between its turns.
    Coil 2 mirrors coil 1, starting from the opposite corner and
    traversing in the reverse direction.

Complexity:
    Time : O(n^2)  - each coil visits 8n^2 cells exactly once
    Space: O(n^2)  - output only; O(1) auxiliary (values computed on the fly)
"""


# --------------------------------------- Solution -----------------------------------------------------


class Solution:
    def formCoils(self, n: int) -> list[list[int]]:
        # code here
        m = 4 * n
        def value(r: int, c: int) -> int:
            return r * m + c + 1
        coil1 = []
        coil2 = []
        top, left = 0, 0
        bottom, right = m - 1, m - 1
        while top <= bottom and left <= right:
            for r in range(top, bottom + 1):
                coil1.append(value(r, left))
            for c in range(left + 1, right):
                coil1.append(value(bottom, c))
            for r in range(bottom - 1, top, -1):
                coil1.append(value(r, right - 1))
            for c in range(right - 2, left + 1, -1):
                coil1.append(value(top + 1, c))
            top += 2
            left += 2
            bottom -= 2
            right -= 2
        top, left = 0, 0
        bottom, right = m - 1, m - 1
        while top <= bottom and left <= right:
            for r in range(bottom, top - 1, -1):
                coil2.append(value(r, right))
            for c in range(right - 1, left, -1):
                coil2.append(value(top, c))
            for r in range(top + 1, bottom):
                coil2.append(value(r, left + 1))
            for c in range(left + 2, right - 1):
                coil2.append(value(bottom - 1, c))
            top += 2
            left += 2
            bottom -= 2
            right -= 2
        return [coil1, coil2]
