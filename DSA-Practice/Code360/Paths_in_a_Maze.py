"""
Problem   : Paths in a Maze
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380921
Difficulty: Easy
Topics    : Backtracking, Recursion, DFS (Depth-First Search), Matrix / Grid
Date      : 2026-09-15

Approach:
    Backtracking / DFS on a grid. Starting from (0,0), explore all four
    directions (Down, Left, Right, Up) in that priority order, marking
    cells visited to avoid revisiting, and backtrack (unmark) after
    exploring each branch. Whenever (n-1, n-1) is reached, the path
    string built so far is recorded. All paths are collected, then
    sorted lexicographically before returning.

Time Complexity : O(4^(n*n)) worst case — each cell can branch into up
                   to 4 directions, and in the worst case (all 1s) the
                   recursion explores most simple paths in the grid.
Space Complexity: O(n^2) for the visited matrix + O(n^2) recursion
                   depth in the worst case, plus O(k*n) for storing k
                   resulting paths of length up to ~n^2.
"""


# -------------------------------- Solution -----------------------------------------------


def findAllPaths(arr):
    n = len(arr)
    result = []
    if n == 0 or arr[0][0] == 0 or arr[n - 1][n - 1] == 0:
        return result
    visited = [[False] * n for _ in range(n)]
    def dfs(x, y, path):
        if x == n - 1 and y == n - 1:
            result.append(path)
            return
        visited[x][y] = True
        directions = [
            (1, 0, 'D'),
            (0, -1, 'L'),
            (0, 1, 'R'),
            (-1, 0, 'U')
        ]
        for dx, dy, move in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n and
                0 <= ny < n and
                arr[nx][ny] == 1 and
                not visited[nx][ny]):
                dfs(nx, ny, path + move)
        visited[x][y] = False
    dfs(0, 0, "")
    result.sort()
    return result
