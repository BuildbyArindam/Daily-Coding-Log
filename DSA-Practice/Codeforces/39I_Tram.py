"""
Problem: Tram
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/39/I
Difficulty: *2500
Topics: Graphs, BFS, Number Theory (GCD)
Date Solved: 2026-09-06

Approach:
  BFS from node 1 to get shortest distances dist[].
  For every edge (u -> v), the "expected" distance to v via u is
  dist[u] + 1, and the mismatch (dist[u] + 1 - dist[v]) must be a
  multiple of the tram's fixed interval t. Taking the GCD of all
  such mismatches across every edge gives t. Camera stops are then
  every node whose distance from the start is a multiple of t.

Time Complexity:  O(n + m) for BFS + O(m log(max_diff)) for GCD accumulation
Space Complexity: O(n + m) for adjacency list (arrays) + distance array
"""


# ----------------------- Solution ------------------------------


import sys
from math import gcd
from array import array

def solve():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    head = array('i', [-1]) * (n + 1)
    to = array('i')
    nxt = array('i')
    for i in range(m):
        u, v = map(int, input().split())
        to.append(v)
        nxt.append(head[u])
        head[u] = i
    dist = array('i', [-1]) * (n + 1)
    dist[1] = 0
    q = array('i', [1])
    ptr = 0
    while ptr < len(q):
        u = q[ptr]
        ptr += 1
        e = head[u]
        while e != -1:
            v = to[e]
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
            e = nxt[e]
    t = 0
    for u in range(1, n + 1):
        if dist[u] == -1:
            continue
        e = head[u]
        while e != -1:
            v = to[e]
            diff = dist[u] + 1 - dist[v]
            t = gcd(t, diff)
            e = nxt[e]
    cameras = []
    for v in range(1, n + 1):
        if dist[v] != -1 and dist[v] % t == 0:
            cameras.append(v)
    sys.stdout.write(str(t) + '\n')
    sys.stdout.write(str(len(cameras)) + '\n')
    sys.stdout.write(' '.join(map(str, cameras)) + '\n')

if __name__ == "__main__":
    solve()
