"""
Problem   : Two Paths (CF14D)
Link      : https://codeforces.com/problemset/problem/14/D
Date      : 2026-08-19
Difficulty: *1900
Topics    : Trees, DFS/BFS, Shortest Paths, DP, Two Pointers

Approach:
For every edge (u, v) in the tree, treat it as the "cut" that splits
the tree into two components. Removing the edge is simulated by
passing (u, v) as a forbidden edge into BFS rather than physically
splitting the adjacency lists. For each side, find the diameter using
the standard two-BFS technique (BFS from any node -> farthest node A,
BFS from A -> farthest node B, diameter = dist(A, B)). Multiply the
two diameters and take the max over all n-1 possible edge removals.

Complexity:
Time : O(n^2)   -> n-1 edges, each doing 2 BFS calls of O(n) each
Space: O(n)     -> adjacency list + visited set/queue per BFS
"""


# ---------------------- Solution ----------------------------


import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    edges = []
    adj = [[] for _ in range(n + 1)]
    idx = 1
    for _ in range(n - 1):
        u, v = int(data[idx]), int(data[idx + 1])
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    def get_farthest(start, forbidden_u, forbidden_v):
        visited = {start}
        queue = [(start, 0)]
        farthest_node = start
        max_dist = 0
        while queue:
            curr, dist = queue.pop(0)
            if dist > max_dist:
                max_dist = dist
                farthest_node = curr
            for neighbor in adj[curr]:
                if (curr == forbidden_u and neighbor == forbidden_v) or (
                    curr == forbidden_v and neighbor == forbidden_u
                ):
                    continue
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return farthest_node, max_dist
    def get_tree_diameter(start, forbidden_u, forbidden_v):
        farthest_node, _ = get_farthest(start, forbidden_u, forbidden_v)
        _, diameter = get_farthest(farthest_node, forbidden_u, forbidden_v)
        return diameter
    max_profit = 0
    for u, v in edges:
        d1 = get_tree_diameter(u, u, v)
        d2 = get_tree_diameter(v, u, v)
        max_profit = max(max_profit, d1 * d2)
    print(max_profit)

if __name__ == "__main__":
    main()
