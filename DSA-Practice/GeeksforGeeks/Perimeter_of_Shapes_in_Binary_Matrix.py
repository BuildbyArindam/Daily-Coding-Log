"""
Problem   : Perimeter of Shapes in Binary Matrix
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/find-perimeter-of-shapes/1
Difficulty: Easy
Topics    : Matrix, Geometric
Date      : 2026-10-04

Approach:
    Every cell with value 1 contributes 4 edges on its own. Each pair of
    adjacent 1s shares an edge that is hidden from the outside, which removes
    2 from the total (1 from each cell). To count each pair once, only check
    the top and left neighbours while scanning row by row.

    perimeter = 4 * (number of 1s) - 2 * (number of adjacent 1-pairs)

Complexity:
    Time : O(n * m), a single pass over the matrix
    Space: O(1), no extra data structures
"""


# ---------------------------------------- Solution --------------------------------------------------------


from typing import List

class Solution:
    def findPerimeter(self, mat: List[List[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])
        perimeter = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    perimeter += 4
                    if i > 0 and mat[i - 1][j] == 1:
                        perimeter -= 2
                    if j > 0 and mat[i][j - 1] == 1:
                        perimeter -= 2
        return perimeter
