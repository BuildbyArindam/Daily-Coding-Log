"""
Problem   : Spanning Tree
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/spanning-tree_624871?kunjiRedirection=true
Date      : 2026-09-11
Difficulty: Medium
Topics    : Minimum Spanning Tree, Kruskal's Algorithm, Disjoint Set Union (Union-Find), Greedy

Approach:
Sort all edges by weight ascending. Use Kruskal's algorithm with a DSU
(union by rank + path compression) to greedily add the smallest edge
that connects two previously disconnected components, skipping edges
that would form a cycle. Stop once n-1 edges are added (a spanning
tree is complete). Sum of accepted edge weights = MST weight.

Time complexity : O(E log E)  -- dominated by sorting edges
Space complexity: O(N + E)    -- DSU arrays + edge list
"""


# -------------------------- Solution ---------------------------------


from math import *
from collections import *
from sys import *
from os import *

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return True

input = stdin.readline
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
edges.sort()
dsu = DSU(n)
total_weight = 0
edges_used = 0
for w, u, v in edges:
    if dsu.union(u, v):
        total_weight += w
        edges_used += 1
        if edges_used == n - 1:
            break
print(total_weight)
