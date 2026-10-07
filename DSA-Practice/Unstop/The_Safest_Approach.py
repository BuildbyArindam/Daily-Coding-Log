"""
Problem   : The Safest Approach
Platform  : Unstop
Link      : https://unstop.com/code/practice/661536
Difficulty: Medium
Date      : 2026-10-07
Topics    : Greedy, Heap (Priority Queue), Sorting, DSU

Approach:
    For each node, find the path from node 1 that minimizes the maximum
    edge weight (the "danger") along the path. This is a minimax path
    problem, solved with Dijkstra where the relaxation cost is
    max(current_danger, edge_weight) instead of a sum. Because this cost is
    monotonic (it never decreases along a path), the greedy
    pop-the-smallest-first invariant of Dijkstra still holds. Unreachable
    nodes output -1.

    (Alternative: sort edges and union them with DSU until 1 and v connect;
    the weight of the last edge added is the answer for v.)

Complexity:
    Time : O((N + M) log N)  (each edge can trigger a heap push)
    Space: O(N + M)          (adjacency list, dist array, heap)
"""


# -------------------------------------------- Solution --------------------------------------------------


import sys
import heapq

def solve():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w)) 
    INF = 10**18
    dist = [INF] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)] 
    while pq:
        current, u = heapq.heappop(pq)
        if current != dist[u]:
            continue
        for v, w in graph[u]:
            new_danger = max(current, w)
            if new_danger < dist[v]:
                dist[v] = new_danger
                heapq.heappush(pq, (new_danger, v))
    result = [str(dist[i]) if dist[i] != INF else "-1" for i in range(1, n + 1)]
    print(" ".join(result))

if __name__ == "__main__":
    solve()
