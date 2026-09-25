# GeeksforGeeks: Box Stacking
# Problem: https://www.geeksforgeeks.org/problems/box-stacking/1
# Date: 2026-09-25
# Difficulty: Hard 
# Topics: Dynamic Programming
#
# Approach:
# - Generate all 3 possible orientations for every box.
# - Normalize the base dimensions as (min, max) so rotations of the base
#   are treated consistently.
# - Use memoized DFS: for each orientation, try placing every orientation
#   with strictly larger base dimensions on top.
# - dp[i] stores the maximum stack height starting from orientation i.
#
# Time Complexity: O(n^2), where n is the number of original boxes.
#                  There are 3n orientations, so this is O((3n)^2).
# Space Complexity: O(n) for the DP array and recursion stack
#                   (with 3n orientations, still O(n)).


# --------------------------------------- Solution ---------------------------------------------


class Solution:
    def maxHeight(self, height: list[int], width: list[int], length: list[int]) -> int:
        # Code here
        boxes = []
        for h, w, l in zip(height, width, length):
            boxes.append((h, min(w, l), max(w, l)))
            boxes.append((w, min(h, l), max(h, l)))
            boxes.append((l, min(h, w), max(h, w)))
        m = len(boxes)
        dp = [0] * m
        def solve(i):
            if dp[i] != 0:
                return dp[i]
            h, w, l = boxes[i]
            best = h
            for j in range(m):
                hj, wj, lj = boxes[j]
                if wj > w and lj > l:
                    best = max(best, h + solve(j))
            dp[i] = best
            return best
        return max(solve(i) for i in range(m))
