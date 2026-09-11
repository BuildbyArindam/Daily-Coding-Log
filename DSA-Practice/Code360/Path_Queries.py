"""
Problem   : Path Queries
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/path-queries_29971?kunjiRedirection=true
Date      : 2026-09-11
Difficulty: Easy
Topics    : Graphs, Dijkstra's Algorithm, All-Pairs Shortest Path

Approach  :
    - Weighted undirected graph with N nodes, M edges, Q shortest-path queries.
    - Run Dijkstra's algorithm from every node once (multi-source Dijkstra),
      precomputing all-pairs shortest distances.
    - Each query is then answered in O(1) by a simple lookup.
    - Unreachable pairs are reported as -1.

Complexity:
    Time  : O(N * (M + N) log N)   -- Dijkstra run N times
    Space : O(N^2)                  -- storing all-pairs shortest distance table
"""


# -------------------------- Solution -----------------------------------


from math import *
from collections import *
from sys import *
from os import *
from heapq import *

data = list(map(int, stdin.buffer.read().split()))
it = iter(data)
N = next(it)
M = next(it)
Q = next(it)
graph = [[] for _ in range(N)]
for _ in range(M):
    u = next(it) - 1
    v = next(it) - 1
    w = next(it)
    graph[u].append((v, w))
    graph[v].append((u, w))
INF = 10**18
shortest = []
for start in range(N):
    dist = [INF] * N
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heappop(pq)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heappush(pq, (nd, v))
    shortest.append(dist)
ans = []
for _ in range(Q):
    u = next(it) - 1
    v = next(it) - 1
    if shortest[u][v] == INF:
        ans.append("-1")
    else:
        ans.append(str(shortest[u][v]))
stdout.write("\n".join(ans))
