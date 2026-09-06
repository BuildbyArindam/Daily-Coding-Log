"""
Problem   : The Lineage Ledger
Platform  : Unstop
Link      : https://unstop.com/code/practice/659242
Date      : 2026-09-06
Difficulty: Medium
Topics    : Tree, Graphs, LCA, Binary Lifting, DFS, Tree Queries, Shortest Path

Approach:
Build the tree from parent-edge input (each node v given with its parent u
and edge weight w). Iteratively compute depth[] and dist[] (weighted
distance from root) for every node via an explicit stack-based walk up to
the nearest already-resolved ancestor (avoids recursion depth issues on
skewed trees). Precompute a binary-lifting table up[k][v] = 2^k-th ancestor
of v for O(log n) LCA queries. For each query (x, y):
  - years  = dist[x] + dist[y] - 2*dist[lca]      (sum of edge weights on path)
  - rulers = depth[x] + depth[y] - 2*depth[lca] + 1  (node count on path)

Time complexity : O(n log n) preprocessing, O(log n) per LCA query
                   -> O((n + q) log n) overall
Space complexity : O(n log n) for the binary lifting table
"""


# -------------------------------- Solution --------------------------------------


import sys
input = sys.stdin.readline
n = int(input())
parent = [0] * (n + 1)
weight = [0] * (n + 1)
parent[1] = 1
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    parent[v] = u
    weight[v] = w
depth = [-1] * (n + 1)
dist = [0] * (n + 1)
depth[1] = 0
for start in range(2, n + 1):
    if depth[start] != -1:
        continue
    path = []
    cur = start
    while depth[cur] == -1:
        path.append(cur)
        cur = parent[cur]
    for node in reversed(path):
        p = parent[node]
        depth[node] = depth[p] + 1
        dist[node] = dist[p] + weight[node]
LOG = n.bit_length()
up = [parent[:]]
for k in range(1, LOG):
    prev = up[-1]
    curr = [0] * (n + 1)
    for v in range(1, n + 1):
        curr[v] = prev[prev[v]]
    up.append(curr)
def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a
    diff = depth[a] - depth[b]
    bit = 0
    while diff:
        if diff & 1:
            a = up[bit][a]
        diff >>= 1
        bit += 1
    if a == b:
        return a
    for k in range(LOG - 1, -1, -1):
        if up[k][a] != up[k][b]:
            a = up[k][a]
            b = up[k][b]
    return up[0][a]
q = int(input())
out = []
for _ in range(q):
    x, y = map(int, input().split())
    common = lca(x, y)
    years = dist[x] + dist[y] - 2 * dist[common]
    rulers = depth[x] + depth[y] - 2 * depth[common] + 1
    out.append(f"{years} {rulers}")
sys.stdout.write("\n".join(out))
