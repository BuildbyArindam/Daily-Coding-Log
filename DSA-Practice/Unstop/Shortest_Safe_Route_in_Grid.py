"""
Problem: Find Shortest Safe Route in a Matrix
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/find-shortest-safe-route-in-a-matrix/1
Date Solved: 2026-09-14
Difficulty: Medium
Topics: BFS, Graph, Matrix

Approach:
    1. Mark every mine cell (0) as unsafe, along with its 4 direct neighbors
       (since stepping adjacent to a mine is also unsafe).
    2. Run a multi-source BFS starting from every safe cell in column 0.
    3. BFS explores cell-by-cell in 4 directions (up/down/left/right),
       tracking distance from start; the first time column (m-1) is reached
       gives the shortest safe path length.
    4. Return -1 if no safe path exists.

Time Complexity:  O(n*m)   -> marking unsafe cells + BFS traversal, each cell visited once
Space Complexity: O(n*m)   -> unsafe grid, dist grid, and BFS queue
"""


# ---------------------------- Solution ----------------------------------------


from collections import deque

class Solution:
    def shortestPath(self, mat: list[list[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])
        unsafe = [[False] * m for _ in range(n)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    unsafe[i][j] = True
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < m:
                            unsafe[ni][nj] = True
        q = deque()
        dist = [[-1] * m for _ in range(n)]
        for i in range(n):
            if not unsafe[i][0]:
                q.append((i, 0))
                dist[i][0] = 1 
        while q:
            i, j = q.popleft()
            if j == m - 1:
                return dist[i][j]
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (
                    0 <= ni < n
                    and 0 <= nj < m
                    and not unsafe[ni][nj]
                    and dist[ni][nj] == -1
                ):
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
        return -1
