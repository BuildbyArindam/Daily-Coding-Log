"""
Problem   : Geek in a Maze
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/geek-in-a-maze--170637/1
Difficulty: Hard
Topic     : Graph (0-1 BFS on a grid)
Date      : 2026-08-23

Approach:
From the start cell, moving UP costs 1 unit of "up-budget" and moving DOWN,
LEFT, RIGHT costs 0. This is a classic 0-1 BFS: use a deque, push 0-cost
moves to the front and 1-cost moves to the back, so the deque always pops
cells in non-decreasing order of cost (min number of "up" moves used to
reach that cell). dist[i][j] stores the minimum number of up-moves needed
to reach cell (i,j) from (r,c). Since every non-up move is free, the
minimum number of down-moves to reach a cell in the same reachable
component is simply (row_offset - up_moves_used), i.e. min_down =
min_up + (i - r). A cell counts toward the answer only if it's reachable
AND min_up <= u AND min_down <= d.

Time complexity : O(n*m)   -- each cell enters the deque a bounded number
                              of times (0-1 BFS relaxation), standard for
                              grid 0-1 BFS.
Space complexity: O(n*m)   -- dist matrix + deque.
"""


# ------------------------- Solution --------------------------------


from collections import deque

class Solution:
    def numberOfCells(self, r: int, c: int, u: int, d: int, mat: list[list[int]]) -> int:
        # code here
        if mat[r][c] == '#':
            return 0
        n = len(mat)
        m = len(mat[0])
        INF = 10**18
        dist = [[INF] * m for _ in range(n)]
        dist[r][c] = 0
        q = deque()
        q.append((r, c))
        directions = [
            (-1, 0, 1),  
            (1, 0, 0),  
            (0, -1, 0), 
            (0, 1, 0)   
        ]
        while q:
            x, y = q.popleft()
            cur_cost = dist[x][y]
            for dx, dy, cost in directions:
                nx = x + dx
                ny = y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if mat[nx][ny] == '#':
                    continue
                new_cost = cur_cost + cost
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    if cost == 0:
                        q.appendleft((nx, ny))
                    else:
                        q.append((nx, ny))
        ans = 0
        for i in range(n):
            for j in range(m):
                if dist[i][j] == INF:
                    continue
                min_up = dist[i][j]
                min_down = min_up + (i - r)
                if min_up <= u and min_down <= d:
                    ans += 1
        return ans
