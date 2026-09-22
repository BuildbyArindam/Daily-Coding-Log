"""
Problem: Special Paths
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/special-path-b3ac37d0/
Date: 2026-09-22
Difficulty: Hard
Topics: Binary Search, Graphs, Algorithms

Approach:
Model the graph with edge weight = |A[u] - A[v]| for each edge (u, v).
Run a modified Dijkstra where instead of summing edge weights along
a path, we track the MAXIMUM edge weight seen so far (bottleneck path).
For each neighbor, new_value = max(curr_value, edge_weight), and we
relax dist[v] only if this bottleneck value is smaller than the best
known bottleneck to v. A min-heap (priority queue) pops the state with
the smallest current bottleneck first, guaranteeing dist[end] is
finalized correctly when popped (same correctness argument as Dijkstra,
since the "distance" function max(a, b) is monotonic non-decreasing
along a path, same as summation).
This effectively finds the path start -> end that minimizes the
largest edge weight on the path (a minimax/bottleneck shortest path),
which is why it fits under "Binary Search on Answer" style problems
(this greedy-heap version replaces the binary-search-over-threshold +
BFS/DFS approach with a single Dijkstra-like pass).

Time Complexity: O((N + M) log N)  — standard Dijkstra with a binary heap
Space Complexity: O(N + M)  — adjacency list + dist array + heap
"""


# ------------------------------------ Solution -------------------------------------------------


import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
edges = []
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v))
A = list(map(int, input().split()))
for u, v in edges:
    w = abs(A[u] - A[v])
    graph[u].append((v, w))
    graph[v].append((u, w))
start, end = map(int, input().split())
start -= 1
end -= 1
dist = [float('inf')] * N
dist[start] = 0
pq = [(0, start)]
while pq:
    curr_value, u = heapq.heappop(pq)
    if curr_value != dist[u]:
        continue
    if u == end:
        print(curr_value)
        break
    for v, w in graph[u]:
        new_value = max(curr_value, w)
        if new_value < dist[v]:
            dist[v] = new_value
            heapq.heappush(pq, (new_value, v))
