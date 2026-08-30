"""
Problem: Bucket Fill 2
Platform: FreeCodeCamp - Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-08
Date Solved: 2026-08-30

Difficulty: Easy-Medium (typical for connected-component/flood-fill counting problems)
Topics: Matrix/Grid, DFS/BFS, Connected Components, Flood Fill, Graph Traversal

Approach:
Traverse every unvisited cell in the grid. For each new cell, flood-fill
(iterative DFS using a stack) through all 4-directionally adjacent cells
of the same color, marking them visited. Each flood-fill call represents
one contiguous colored region. Every region whose color differs from the
target_color requires one "click" to repaint it toward the target.
Sum these clicks across all regions.

Time Complexity:  O(rows * cols) — each cell is visited and pushed/popped
                   from the stack at most once.
Space Complexity: O(rows * cols) — for the visited set and the DFS stack
                   in the worst case (a single large region).
"""


# ----------------------------- Solution --------------------------------------


def bucket_fill(grid, target_color):
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    clicks = 0
    for r in range(rows):
        for c in range(cols):
            if (r, c) in visited:
                continue
            color = grid[r][c]
            stack = [(r, c)]
            visited.add((r, c))
            while stack:
                x, y = stack.pop()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < rows and
                        0 <= ny < cols and
                        (nx, ny) not in visited and
                        grid[nx][ny] == color):
                        visited.add((nx, ny))
                        stack.append((nx, ny))
            if color != target_color:
                clicks += 1
    return clicks
