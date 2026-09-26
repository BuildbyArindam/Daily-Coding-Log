"""
Problem   : Corridors of the Kestrel Station
Platform  : Unstop
Link      : https://unstop.com/code/practice/661019
Date      : 2026-09-26
Difficulty: Easy
Topics    : Graph, DSU (Union-Find), Sorting, Offline Queries, Dynamic Connectivity

Approach:
    Offline query processing with Union-Find (Kruskal-style).
    - Sort edges by cost, sort queries by budget.
    - Sweep through queries in increasing order of budget, unioning all
      edges whose cost <= current budget before answering that query.
    - Since budgets only increase during the sweep, edges once unioned
      never need to be revisited (two-pointer over sorted edges).
    - For each query, check if the two nodes share the same DSU root.

Time Complexity : O((N + M) log M + Q log Q)   [sorting edges/queries + union-find ops]
Space Complexity: O(N + M + Q)
"""


# -------------------------------------- Solution ---------------------------------------------------


import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

def main():
    input = sys.stdin.readline
    n, m, q = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, cost = map(int, input().split())
        edges.append((cost, u, v))
    queries = []
    for i in range(q):
        a, b, budget = map(int, input().split())
        queries.append((budget, a, b, i))
    edges.sort()
    queries.sort()
    dsu = DSU(n)
    answers = ["NO"] * q
    edge_ptr = 0
    for budget, a, b, idx in queries:
        while edge_ptr < m and edges[edge_ptr][0] <= budget:
            _, u, v = edges[edge_ptr]
            dsu.union(u, v)
            edge_ptr += 1
        if dsu.find(a) == dsu.find(b):
            answers[idx] = "YES"
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()
