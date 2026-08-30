"""
Problem   : The Punctual Line
Platform  : Unstop
Link      : https://unstop.com/code/practice/658900
Difficulty: Hard
Date      : 2026-08-30

Approach:
    Modified Dijkstra over a graph where each edge represents a scheduled
    bus/train line (first departure, frequency, duration). At each node,
    for every outgoing edge, compute the earliest valid departure time
    given the current arrival time (either the fixed one-shot departure
    when freq == 0, or the next periodic slot >= current time via
    ceiling division). Push (arrival_time, node) into a min-heap and
    relax as in standard Dijkstra, tracking earliest arrival dist[].

    Note: solved as a time-expanded shortest-path problem; the listed
    topics (Fenwick/BIT, Mo's Algorithm) reflect Unstop's tag set for
    this problem, not the technique actually used here.

Time complexity : O((N + M) log N) — standard Dijkstra with a binary heap
Space complexity: O(N + M) — adjacency list + dist array + heap
"""


# ----------------------- Solution ----------------------


import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, S, D = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, first, freq, dur = map(int, input().split())
        graph[u].append((v, first, freq, dur))
    INF = 10**30
    dist = [INF] * (n + 1)
    dist[S] = 0
    pq = [(0, S)] 
    while pq:
        t, u = heapq.heappop(pq)
        if t != dist[u]:
            continue
        if u == D:
            print(t)
            return
        for v, first, freq, dur in graph[u]:
            if freq == 0:
                if first < t:
                    continue
                depart = first
            else:
                if t <= first:
                    depart = first
                else:
                    k = (t - first + freq - 1) // freq
                    depart = first + k * freq
            arrival = depart + dur
            if arrival < dist[v]:
                dist[v] = arrival
                heapq.heappush(pq, (arrival, v))
    print(-1)

if __name__ == "__main__":
    solve()
