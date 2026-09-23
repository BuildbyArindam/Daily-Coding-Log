"""
Problem: Little Monk and Edge Count
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/codemonk/8/1483398/
Date Solved: 2026-09-23
Difficulty: Medium
Topics: Trees, DFS, Subtree Size, Edge Contribution Counting

Approach:
Root the tree at node 1 and do an iterative DFS to compute parent, the
edge id connecting each node to its parent, and a post-order visitation
list. Process nodes in reverse post-order to compute subtree sizes
bottom-up. For each non-root node u, removing the edge to its parent
splits the tree into a subtree of size `s = subtree[u]` and the rest
of size `N - s`. The number of node pairs separated by that cut is
s * (N - s), which is precomputed once and answered in O(1) per query.

Time Complexity: O(N + Q) — single DFS pass to build subtree sizes,
                  O(1) per query lookup.
Space Complexity: O(N) — adjacency list, parent/subtree/answer arrays.
"""


# ------------------------------------------ Solution ----------------------------------------


import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for edge_id in range(1, N):
    a, b = map(int, input().split())
    adj[a].append((b, edge_id))
    adj[b].append((a, edge_id))
parent = [0] * (N + 1)
parent_edge = [0] * (N + 1)
order = []
stack = [1]
parent[1] = -1
while stack:
    u = stack.pop()
    order.append(u)
    for v, edge_id in adj[u]:
        if v == parent[u]:
            continue
        parent[v] = u
        parent_edge[v] = edge_id
        stack.append(v)
subtree = [1] * (N + 1)
for u in reversed(order):
    if parent[u] > 0:
        subtree[parent[u]] += subtree[u]
answer = [0] * N
for u in range(2, N + 1):
    edge_id = parent_edge[u]
    s = subtree[u]
    answer[edge_id] = s * (N - s)
out = []
for _ in range(Q):
    x = int(input())
    out.append(str(answer[x]))
sys.stdout.write("\n".join(out))
