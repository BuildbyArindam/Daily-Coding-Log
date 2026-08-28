# Problem: Maze Obstacles
# Link: https://www.naukri.com/code360/problems/maze-obstacles_624776
# Platform: Code360 | Difficulty: Hard
# Date: 2026-08-28
# Topics: Dynamic Programming, Grid Path Counting, Space Optimization
#
# Approach:
#   Count paths from (0,0) to (n-1,m-1) moving only right/down, avoiding
#   cells marked -1. Use a rolling 1D DP array (size m) instead of a full
#   2D table: dp[j] before update = value from the row above (top);
#   after adding dp[j-1] (already updated, i.e. left neighbor) it becomes
#   dp[j] = top + left. Obstacle cells reset dp[j] = 0.
#
# Time Complexity:  O(n * m)
# Space Complexity: O(m)  (rolling array, no full grid DP table needed)


# ------------------------- Solution ------------------------------


from math import *
from collections import *
from sys import *
from os import *

data = list(map(int, stdin.read().split()))
n = data[0]
m = data[1]
maze = []
k = 2
for i in range(n):
    maze.append(data[k:k + m])
    k += m
dp = [0] * m
for i in range(n):
    for j in range(m):
        if maze[i][j] == -1:
            dp[j] = 0
        elif i == 0 and j == 0:
            dp[j] = 1
        else:
            if j > 0:
                dp[j] += dp[j - 1]
print(dp[m - 1])
