# Problem: Signal Codes of the Nightfall Fleet (Max Rectangle of 1s with Column Swaps Allowed)
# Link: https://www.geeksforgeeks.org/problems/find-the-largest-rectangle-of-1s-with-swapping-of-columns-allowed0243/1
# Platform: GeeksforGeeks
# Difficulty: Hard
# Date: 2026-08-27
#
# Approach:
#   Build a running histogram of column heights row by row (consecutive 1s
#   ending at the current row, reset to 0 on a 0). Since columns can be
#   freely reordered, sort each row's heights in descending order — the
#   best rectangle using the k tallest columns has width k and height
#   equal to the k-th tallest, so check area = height[j] * (j + 1) for
#   every j after sorting, and track the max across all rows.
#
# Time Complexity:  O(n * m log m)  -- n rows, sort of m columns each row
# Space Complexity: O(m)            -- heights array (+ O(m) for sort copy)


# ------------------------------ Solution ----------------------------------


class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])
        heights = [0] * m
        ans = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            curr = sorted(heights, reverse=True)
            for j in range(m):
                area = curr[j] * (j + 1)
                ans = max(ans, area)
        return ans
