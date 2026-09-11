"""
Problem: Rat In A Maze
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/rat-in-a-maze_626599?kunjiRedirection=true
Difficulty: Medium
Topics: Backtracking, Recursion, DFS, Matrix Traversal
Date Solved: 2026-09-11

Approach:
Standard DFS/backtracking from (0,0) to (n-1,n-1). At each cell, try all
4 directions (up, down, left, right); recurse into any unvisited, open
(value == 1) cell. Mark cells visited before recursing to avoid revisiting;
backtrack automatically since 'visited' isn't reset (this variant only
needs existence of a path, not the path itself, so no explicit un-marking
is required).

Time Complexity: O(3^(n^2)) worst case — at each step, at most 3 new
directions are viable (the 4th leads back to the visited parent).
Space Complexity: O(n^2) — for the visited matrix + O(n^2) recursion
stack depth in the worst case.
"""


# ------------------------ Solution -------------------------------------


def is_path_possible(maze, n):
    if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
        return False
    visited = [[False] * n for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(row, col):
        if row == n - 1 and col == n - 1:
            return True
        visited[row][col] = True
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            if (0 <= new_row < n and
                0 <= new_col < n and
                maze[new_row][new_col] == 1 and
                not visited[new_row][new_col]):
                if dfs(new_row, new_col):
                    return True
        return False
    return dfs(0, 0)
n = int(input())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().split())))
print(str(is_path_possible(maze, n)).lower())
