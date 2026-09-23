"""
Problem: Learning Graph
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/codemonk/8/1483395/
Date Solved: 2026-09-23
Difficulty: Easy
Topics: Graphs, Adjacency List, Sorting

Approach:
Build an undirected adjacency list from the M edges. For each node i,
if its degree is less than k, no k-th largest neighbor exists -> -1.
Otherwise, sort i's neighbors by (value, node_id) descending and pick
the k-th element (index k-1) as the k-th largest-valued neighbor.

Time Complexity:  O(N + M log M) — each node's neighbor list of size d_i
                  is sorted in O(d_i log d_i); summed over all nodes this
                  is bounded by O(M log M) since sum(d_i) = 2M.
Space Complexity: O(N + M) — adjacency list storage plus value/answer arrays.
"""


# --------------------------------------- Solution ---------------------------------------------


import sys
input = sys.stdin.buffer.readline
N, M, k = map(int, input().split())
val = [0] + list(map(int, input().split()))
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
answer = []
for i in range(1, N + 1):
    if len(adj[i]) < k:
        answer.append("-1")
        continue
    adj[i].sort(key=lambda node: (val[node], node), reverse=True)
    answer.append(str(adj[i][k - 1]))
sys.stdout.write("\n".join(answer))
