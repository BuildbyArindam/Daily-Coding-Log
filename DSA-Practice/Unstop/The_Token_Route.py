"""
Problem   : The Token Route
Platform  : Unstop
Link      : https://unstop.com/code/practice/659276
Difficulty: Medium
Date      : 2026-09-07
Topics    : Graph, Dijkstra's Algorithm, Shortest Path, Priority Queue,
            State Compression, Layered Graph, State-Space Shortest Path

Approach:
    Standard Dijkstra extended with an extra state dimension "used" =
    number of free-token edges consumed so far (0..k). Each node is
    effectively split into (k+1) layers. From state (u, used):
      - Take edge u->v normally: cost increases by w, state stays "used".
      - Take edge u->v "for free" (spend one token): cost stays the
        same, state becomes "used+1" (only if used < k).
    dist[v][used] tracks the shortest cost to reach v having spent
    exactly `used` tokens. Answer is the first time dst is popped from
    the min-heap (since Dijkstra pops in increasing cost order).

Complexity:
    Time : O((N * K + M * K) * log(N * K))   — each of the N*(K+1)
           states relaxes up to 2 outgoing transitions per real edge,
           pushed/popped from a heap of size O(M*K).
    Space: O(N * K) for the dist table + O(M) for the adjacency list.
"""


# ---------------------- Solution -----------------------------


import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, k, src, dst = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    INF = 10**30
    dist = [[INF] * (k + 1) for _ in range(n + 1)]
    dist[src][0] = 0
    pq = [(0, src, 0)]
    while pq:
        cost, u, used = heapq.heappop(pq)
        if cost != dist[u][used]:
            continue
        if u == dst:
            print(cost)
            return
        for v, w in graph[u]:
            new_cost = cost + w
            if new_cost < dist[v][used]:
                dist[v][used] = new_cost
                heapq.heappush(pq, (new_cost, v, used))
            if used < k and cost < dist[v][used + 1]:
                dist[v][used + 1] = cost
                heapq.heappush(pq, (cost, v, used + 1))
    print(-1)

if __name__ == "__main__":
    solve()
