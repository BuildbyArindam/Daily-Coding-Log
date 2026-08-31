"""
Problem   : The Coral Relay
Platform  : Unstop
Link      : https://unstop.com/code/practice/659208
Date      : 2026-08-31
Difficulty: Medium
Topics    : Graph, MST, Kruskal's Algorithm, DSU (Union-Find), Greedy, Sorting, Tree

Approach:
    Classic Minimum Spanning Tree problem solved via Kruskal's algorithm.
    - Sort all m edges by weight (ascending).
    - Use a Disjoint Set Union (Union by Size + Path Compression) to greedily
      pick the smallest edge that connects two previously disconnected
      components, skipping edges that would form a cycle.
    - Stop once (n - 1) edges are added (a spanning tree is complete).
    - If fewer than (n - 1) edges could be added, the graph is disconnected
      and no spanning tree exists -> print -1.

Time Complexity : O(m log m)  -- dominated by sorting edges;
                                 DSU ops are ~O(alpha(n)) (inverse Ackermann, effectively O(1))
Space Complexity: O(n + m)    -- edge list + DSU parent/size arrays
"""


# ----------------------------------- Solution -------------------------------------


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
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()
    dsu = DSU(n)
    total_cost = 0
    edges_used = 0
    for w, u, v in edges:
        if dsu.union(u, v):
            total_cost += w
            edges_used += 1
            if edges_used == n - 1:
                break
    if edges_used != n - 1:
        print(-1)
    else:
        print(total_cost)

if __name__ == "__main__":
    main()
