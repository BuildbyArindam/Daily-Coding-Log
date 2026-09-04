"""
Problem   : Trial for Chief
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/37/E
Difficulty: *2600
Topics    : Graphs, Greedy, Shortest Paths
Date      : 2026-09-04

Approach:
    1. Compress the grid into monochromatic connected components (BFS/flood fill).
    2. Build an adjacency graph over components — an edge between any two
       components that share a border (cost 1 "color-flip" to cross).
    3. Since the board starts all-white, the number of operations to turn a
       target component x into a *contiguous white/black region reachable from
       start* equals dist(start, x) if x is White, or dist(start, x) + 1 if
       x is Black (one extra flip to paint it black at the end).
    4. Run a multi-source-style BFS from every component as a candidate start,
       track the worst-case (max) cost over all components reached from it,
       and take the minimum such worst-case value over all starts.

Time complexity : O((n*m) * (n*m)) in the worst case —
                   O(n*m) components, each triggering an O(n*m) BFS over the
                   component graph (V + E where V, E = O(n*m)).
Space complexity: O(n*m) for comp[][], color[], and the adjacency graph.
"""


# ------------------------- Solution --------------------------------


import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    comp = [[-1] * m for _ in range(n)]
    color = []
    component_count = 0
    for i in range(n):
        for j in range(m):
            if comp[i][j] != -1:
                continue
            c = grid[i][j]
            q = [(i, j)]
            comp[i][j] = component_count
            for x, y in q:
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if (
                        0 <= nx < n
                        and 0 <= ny < m
                        and comp[nx][ny] == -1
                        and grid[nx][ny] == c
                    ):
                        comp[nx][ny] = component_count
                        q.append((nx, ny))
            color.append(c)
            component_count += 1
    graph = [[] for _ in range(component_count)]
    for i in range(n):
        for j in range(m):
            u = comp[i][j]
            if i + 1 < n:
                v = comp[i + 1][j]
                if u != v:
                    graph[u].append(v)
                    graph[v].append(u)
            if j + 1 < m:
                v = comp[i][j + 1]
                if u != v:
                    graph[u].append(v)
                    graph[v].append(u)
    answer = 10**9
    dist = [-1] * component_count
    for start in range(component_count):
        for i in range(component_count):
            dist[i] = -1
        dist[start] = 0
        q = deque([start])
        best = 0
        while q:
            u = q.popleft()
            d = dist[u]
            if color[u] == 'B':
                value = d + 1
            else:
                value = d
            if value > best:
                best = value
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = d + 1
                    q.append(v)
        answer = min(answer, best)
    print(answer)

if __name__ == "__main__":
    solve()
