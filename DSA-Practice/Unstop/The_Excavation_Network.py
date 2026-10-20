"""
Problem   : The Excavation Network
Platform  : Unstop
Link      : https://unstop.com/code/practice/664311
Date      : 2026-10-20
Difficulty: Medium
Topics    : Graphs, DSU / Union-Find, Sorting, Hashing, Greedy

Approach:
    Run Kruskal's algorithm with DSU (path compression + union by size) over
    the edges sorted by cost. This builds a minimum spanning forest, and the
    cost of every edge that merges two components is added to the total.
    Then group nodes by their DSU root, pick the largest component (ties
    broken by the smallest node index), and use a Counter to find its most
    frequent category (ties broken by the smallest category value).

Output: total MST-forest cost, size of the largest component,
        its most frequent category, and that category's frequency.

Complexity:
    Time : O(M log M + N * α(N))  -> sorting dominates
    Space: O(N + M)
"""


# -------------------------------------------------- Solution -------------------------------------------------------------


import sys
from collections import Counter
input = sys.stdin.readline
n, m = map(int, input().split())
categories = list(map(int, input().split()))
edges = []
for _ in range(m):
    u, v, cost = map(int, input().split())
    edges.append((cost, u - 1, v - 1))
edges.sort()
parent = list(range(n))
size = [1] * n
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(u, v):
    root_u = find(u)
    root_v = find(v)
    if root_u == root_v:
        return False
    if size[root_u] < size[root_v]:
        root_u, root_v = root_v, root_u
    parent[root_v] = root_u
    size[root_u] += size[root_v]
    return True
total_cost = 0
for cost, u, v in edges:
    if union(u, v):
        total_cost += cost
components = {}
for i in range(n):
    root = find(i)
    if root not in components:
        components[root] = []
    components[root].append(i)
largest_component = min(
    components.values(),
    key=lambda component: (-len(component), min(component))
)
counts = Counter(categories[i] for i in largest_component)
most_frequent_category, frequency = min(
    counts.items(),
    key=lambda item: (-item[1], item[0])
)
print(total_cost, len(largest_component),
      most_frequent_category, frequency)
