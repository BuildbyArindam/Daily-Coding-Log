"""
Problem: Bucket Fill
Platform: FreeCodeCamp - Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-05
Date Solved: 2026-08-31
Difficulty: Easy-Medium
Topics: BFS/DFS, Flood Fill, Matrix/Grid Traversal, Connected Components, Simulation, Stack (iterative DFS)

Approach:
Iterative DFS (flood fill) using an explicit stack. Starting from `pos`,
repeatedly pop a cell, and push any of its 4-directional neighbors that
still hold the original color, recoloring them to `new_value` as they're
pushed. Avoids recursion depth issues on large grids.

Time Complexity:  O(R * C) - each cell is visited and pushed at most once
Space Complexity: O(R * C) - worst case stack size when the whole grid
                  is one connected region of old_value
"""


# --------------------------- Solution ----------------------------------


def bucket_fill(grid, pos, new_value):
    row, col = pos
    old_value = grid[row][col]
    if old_value == new_value:
        return grid
    rows = len(grid)
    cols = len(grid[0])
    stack = [(row, col)]
    grid[row][col] = new_value
    while stack:
        r, c = stack.pop()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and
                0 <= nc < cols and
                grid[nr][nc] == old_value):
                grid[nr][nc] = new_value
                stack.append((nr, nc))
    return grid
