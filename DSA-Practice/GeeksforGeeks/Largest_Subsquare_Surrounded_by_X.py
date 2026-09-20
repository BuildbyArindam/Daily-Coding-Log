"""
Problem   : Largest Subsquare Surrounded by X
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/largest-subsquare-surrounded-by-x0558/1
Difficulty: Medium
Topics    : Matrix, Dynamic Programming
Date      : 2026-09-20

Approach:
  Precompute two DP matrices:
    - right[i][j] = count of consecutive 'X's to the right of (i,j) in the same row (inclusive)
    - down[i][j]  = count of consecutive 'X's below (i,j) in the same column (inclusive)
  For each cell (i,j), the largest possible square with top-left at (i,j) is
  bounded by min(right[i][j], down[i][j]). Check decreasing candidate sizes
  and confirm the square's border is fully 'X' using the bottom row's
  right[] value and the right column's down[] value.

Time Complexity : O(n^3) worst case (n^2 cells * up to n size checks each,
                   though the early break on first valid size keeps it fast
                   in practice)
Space Complexity: O(n^2) for the two auxiliary DP matrices
"""


# ---------------------------------------- Solution ------------------------------------------------


class Solution:
    def largestSubsquare(self, mat):
        # code here
        n = len(mat)
        right = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 'X':
                    right[i][j] = 1
                    down[i][j] = 1
                    if j + 1 < n:
                        right[i][j] += right[i][j + 1]
                    if i + 1 < n:
                        down[i][j] += down[i + 1][j]
        ans = 0
        for i in range(n):
            for j in range(n):
                max_size = min(right[i][j], down[i][j])
                for size in range(max_size, ans, -1):
                    bottom = i + size - 1
                    right_col = j + size - 1
                    if (down[i][right_col] >= size and
                            right[bottom][j] >= size):
                        ans = size
                        break
        return ans
