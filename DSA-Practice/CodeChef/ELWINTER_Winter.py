"""
Problem   : Winter (ELWINTER)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/ELWINTER
Difficulty: 2007
Date      : 2026-10-20
Topics    : Graph, BFS, Dijkstra-style simulation, Priority Queue

Approach:
    Each node stores the earliest time it freezes (freeze_time). A freeze at
    node u at time t freezes its neighbours at t + 1, so propagation is a
    time-ordered BFS. A min-heap holds (freeze_time, node), and we only expand
    entries with time <= current_time, so propagation is lazy and stops at the
    present moment.
      - Type 1: freeze x at current_time (if that improves freeze_time[x]), then propagate.
      - Type 2: advance current_time by x, then propagate.
      - Type 3: answer YES if freeze_time[x] <= current_time, else NO.
    Stale heap entries are skipped by checking t != freeze_time[u].

Complexity:
    Time : O((N + M + Q) log N) amortized, since each freeze_time improvement
           costs one heap push and relaxations are bounded by edge scans.
    Space: O(N + M) for the graph, distances and heap.
"""


# ---------------------------------------------------- Solution -------------------------------------------------------


import sys
import heapq

input = sys.stdin.readline
N, M, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
INF = 10**18
freeze_time = [INF] * (N + 1)
pq = []
current_time = 0
answers = []

def propagate():
    while pq and pq[0][0] <= current_time:
        t, u = heapq.heappop(pq)
        if t != freeze_time[u]:
            continue
        next_time = t + 1
        for v in graph[u]:
            if next_time < freeze_time[v]:
                freeze_time[v] = next_time
                heapq.heappush(pq, (next_time, v))
for _ in range(Q):
    query_type, x = map(int, input().split())
    if query_type == 1:
        if current_time < freeze_time[x]:
            freeze_time[x] = current_time
            heapq.heappush(pq, (current_time, x))
        propagate()
    elif query_type == 2:
        current_time += x
        propagate()
    else:
        if freeze_time[x] <= current_time:
            answers.append("YES")
        else:
            answers.append("NO")
sys.stdout.write("\n".join(answers))
