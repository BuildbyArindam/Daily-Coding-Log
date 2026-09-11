"""
Problem   : Rotten Oranges
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/rotten-oranges_277629
Difficulty: Hard
Date      : 2026-09-11
Topics    : Multi-source BFS, Graph Traversal, Matrix

Approach:
- Push all initially rotten oranges (2) into a queue as BFS sources.
- Level-by-level (multi-source) BFS: each round represents one unit of time.
- For every rotten orange, rot adjacent fresh oranges (1 -> 2), decrement
  the fresh count, and enqueue the newly rotten ones for the next round.
- Stop when queue empties; if any fresh oranges remain, rotting never
  reached them -> return -1. Otherwise return elapsed time.

Time Complexity : O(N*M)  -- each cell is visited and enqueued at most once
Space Complexity: O(N*M)  -- queue can hold up to all cells in the worst case
"""


# -------------------------- Solution --------------------------------


from collections import deque
import sys
def minimum_time_to_rot(grid, n, m):
    q = deque()
    fresh = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1
    if fresh == 0:
        return 0
    time = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        size = len(q)
        rotted = False
        for _ in range(size):
            x, y = q.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh -= 1
                    q.append((nx, ny))
                    rotted = True
        if rotted:
            time += 1
    return time if fresh == 0 else -1
data = sys.stdin.read().strip().split()
if data:
    n = int(data[0])
    m = int(data[1])
    grid = []
    index = 2
    for _ in range(n):
        row = list(map(int, data[index:index + m]))
        grid.append(row)
        index += m
    print(minimum_time_to_rot(grid, n, m))
