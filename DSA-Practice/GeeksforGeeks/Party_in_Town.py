"""
Problem: Party in Town
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/party-in-town3951/1
Difficulty: Medium
Topic: DFS/BFS, Tree
Date Solved: 2026-09-13

Approach:
Find the tree's diameter using the classic "double BFS" trick:
1. BFS from any arbitrary node to find the farthest node from it (call it `farthest_node`).
2. BFS again from `farthest_node` to find the actual farthest distance — this gives the
   diameter of the tree.
3. The node that minimizes the maximum distance to all others (the "party house") lies
   at the center of the diameter path, so the answer is ceil(diameter / 2),
   computed here as (diameter + 1) // 2.

Time Complexity: O(V + E) — two BFS traversals over the tree
Space Complexity: O(V) — dist array + queue
"""


# ---------------------------- Solution -------------------------------------


from collections import deque

class Solution:
    def partyHouse(self, adj: list[list[int]]) -> int:
        # code here
        n = len(adj)
        def bfs(start):
            dist = [-1] * (n + 1)
            dist[start] = 0
            q = deque([start])
            farthest = start
            while q:
                u = q.popleft()
                if dist[u] > dist[farthest]:
                    farthest = u
                for v in adj[u - 1]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return farthest, dist[farthest]
        farthest_node, _ = bfs(1)
        _, diameter = bfs(farthest_node)
        return (diameter + 1) // 2
