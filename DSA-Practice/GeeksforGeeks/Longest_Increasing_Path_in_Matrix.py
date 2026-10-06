"""
Problem   : Longest Increasing Path in Matrix
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/longest-increasing-path-in-a-matrix/1
Difficulty: Hard
Topics    : Dynamic Programming, Graph, Topological Sort
Date      : 2026-10-06

Approach  : Treat each cell as a node, with a directed edge from a cell to any
            adjacent cell holding a strictly larger value. This graph is a DAG,
            so Kahn's algorithm (BFS topological sort) applies.
            - indegree[i][j] = number of strictly smaller neighbours.
            - Cells with indegree 0 are the starting points of paths.
            - dp[i][j] = longest increasing path ending at (i, j); relaxed as
              dp[nbr] = max(dp[nbr], dp[cur] + 1) while processing in
              topological order.
            - Answer = max value in dp.

Complexity: Time  O(n * m)  -> each cell and its 4 edges are visited a constant number of times
            Space O(n * m)  -> indegree, dp, and the queue
"""


# --------------------------------------------- Solution -----------------------------------------------------------


from collections import deque

class Solution:
    def longIncPath(self, matrix, n, m):
        # code here
        indegree = [[0] * m for _ in range(n)]
        dp = [[1] * m for _ in range(n)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(n):
            for j in range(m):
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        if matrix[ni][nj] < matrix[i][j]:
                            indegree[i][j] += 1
        q = deque()
        for i in range(n):
            for j in range(m):
                if indegree[i][j] == 0:
                    q.append((i, j))
        ans = 1
        while q:
            i, j = q.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    if matrix[ni][nj] > matrix[i][j]:
                        dp[ni][nj] = max(dp[ni][nj], dp[i][j] + 1)
                        indegree[ni][nj] -= 1
                        if indegree[ni][nj] == 0:
                            q.append((ni, nj))
                        ans = max(ans, dp[ni][nj])
        return ans
