"""
Problem: Negative Weight Cycle
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/negative-weight-cycle3504/1
Date: 2026-08-26
Difficulty: Medium
Topic: Graph

Approach:
Bellman-Ford relaxation over V-1 iterations to find shortest distances
from an implicit source (all dist initialized to 0, acting as a virtual
source connected to every node with weight 0). Run one extra (Vth)
iteration — if any edge can still be relaxed, a negative weight cycle
exists reachable from that virtual source.

Time Complexity: O(V * E)
Space Complexity: O(V)
"""


# ----------------------------- Solution -----------------------------------


class Solution:
    def isNegativeWeightCycle(self, V: int, edges: list[list[int]]) -> bool:
        # code here
        dist = [0] * V
        for i in range(V):
            updated = False
            for u, v, w in edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
                    if i == V - 1:
                        return True
            if not updated:
                break
        return False
