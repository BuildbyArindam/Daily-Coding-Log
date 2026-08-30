"""
Problem: Mail Stamps
Link: https://codeforces.com/problemset/problem/29/C
Platform: Codeforces | Difficulty: *1700
Topics: Data Structures, DFS and Similar, Graphs, Implementation
Date: 2026-08-30

Approach:
Each envelope (a, b) is an undirected edge between cities. The full sequence
of envelopes forms a single path (a chain), since every city has at most
2 connections except the two endpoints, which have exactly 1. Build an
adjacency list, find one endpoint (degree == 1), then walk the chain from
there, always moving to the neighbor that isn't where we came from.

Time Complexity: O(n) — build graph once, traverse each edge once
Space Complexity: O(n) — adjacency list + route list
"""


# --------------------------- Solution -----------------------------


import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    graph = {}
    for _ in range(n):
        a, b = map(int, input().split())
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    start = next(city for city in graph if len(graph[city]) == 1)
    route = []
    current = start
    previous = None
    while current is not None:
        route.append(current)
        next_city = None
        for neighbor in graph[current]:
            if neighbor != previous:
                next_city = neighbor
                break
        previous, current = current, next_city
    print(*route)

if __name__ == "__main__":
    solve()
