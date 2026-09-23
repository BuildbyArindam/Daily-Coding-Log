"""
Platform    : Unstop
Problem     : Rzepin Dispatch Ceiling
Link        : https://unstop.com/code/practice/660870
Difficulty  : Hard
Date Solved : 2026-09-23
Topics      : Graph, Dijkstra, Shortest Path, Priority Queue, State Compression

Approach:
    Resource-constrained shortest path. Expand each node into (node, turbulence_used)
    states, encoded as a single int: node * (R + 1) + turb. Run Dijkstra from
    (source, 0) minimising total fuel, and prune any transition where cumulative
    turbulence would exceed R. Afterwards, take a prefix minimum over the turbulence
    dimension for each node, so dist[node][t] means "min fuel using AT MOST t turbulence".
    Each query (dest, tolerance) is then answered in O(1).

Complexity (W = R + 1):
    Time  : O(m * W * log(n * W)) for Dijkstra, plus O(n * W) for the prefix-min
            pass and O(q) for queries
    Space : O(n * W) for the dist array, plus O(m) for the graph
"""


# --------------------------------------------------- Solution ---------------------------------------------------


import sys 
import heapq
input = sys.stdin.buffer.readline

n, m, R = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, fuel, turb = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, fuel, turb))
W = R + 1
INF = 10**18
dist = [INF] * (n * W)
dist[0] = 0
pq = [(0, 0)]
while pq:
    fuel, state = heapq.heappop(pq)
    if fuel != dist[state]:
        continue
    node = state // W
    turb_used = state % W
    for nxt, edge_fuel, edge_turb in graph[node]:
        new_turb = turb_used + edge_turb
        if new_turb > R:
            continue
        new_state = nxt * W + new_turb
        new_fuel = fuel + edge_fuel
        if new_fuel < dist[new_state]:
            dist[new_state] = new_fuel
            heapq.heappush(pq, (new_fuel, new_state))
for node in range(n):
    base = node * W
    best = INF
    for turb in range(W):
        if dist[base + turb] < best:
            best = dist[base + turb]
        dist[base + turb] = best
q = int(input())
out = []
for _ in range(q):
    dest, tolerance = map(int, input().split())
    dest -= 1
    ans = dist[dest * W + tolerance]
    if ans >= INF:
        out.append(str("-1"))
    else:
        out.append(str(ans))
sys.stdout.write("\n".join(out))
