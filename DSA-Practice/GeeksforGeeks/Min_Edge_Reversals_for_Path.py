"""
Problem: Min Edge Reversals for Path
Link: https://www.geeksforgeeks.org/problems/minimum-edges/1
Platform: GeeksforGeeks
Date: 2026-09-17
Difficulty: Medium
Topics: Graph, Deque (0-1 BFS)

Approach:
Build a directed graph where original edges cost 0 (traversed in given
direction) and reversed edges cost 1 (traversed against given direction).
Run a 0-1 BFS (deque-based Dijkstra variant) from src: push 0-cost edges
to the front of the deque and 1-cost edges to the back, so the deque
stays sorted by distance without needing a priority queue. dist[dst]
gives the minimum number of edge reversals needed to reach dst from src.

Time Complexity:  O(V + E)   -- each edge relaxed at most once, deque ops O(1)
Space Complexity: O(V + E)   -- adjacency list + dist array + deque
"""


# --------------------------------- Solution ----------------------------------------


from collections import deque

class Solution:
    def minimumEdgeReversal(self, edges: list[list[int]], n: int, src: int, dst: int) -> int:
        # code here
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append((v, 0))
            graph[v].append((u, 1))
        dist = [float('inf')] * (n + 1)
        dist[src] = 0
        dq = deque([src])
        while dq:
            u = dq.popleft()
            for v, cost in graph[u]:
                new_dist = dist[u] + cost
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    if cost == 0:
                        dq.appendleft(v)
                    else:
                        dq.append(v)
        return -1 if dist[dst] == float('inf') else dist[dst]
