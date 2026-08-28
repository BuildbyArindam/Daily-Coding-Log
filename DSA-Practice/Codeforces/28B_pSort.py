"""
Problem: pSort
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/28/B
Difficulty: *1600
Date Solved: 2026-08-28
Topics: DFS and Similar, DSU, Graphs

Approach:
Person i can eventually reach position (i - d[i]) or (i + d[i]) via
repeated swaps of distance d[i], and this holds transitively (once i
is connected to j, i can also use d[j]). So union i with (i - d[i])
and (i + d[i]) for every i, building connectivity components over
positions using DSU. A valid sort is achievable iff, for every
position i, the person currently at i (p[i]) belongs to the same
component as its target position (p[i] - 1) — since p[i] must end up
at index p[i] - 1 in the final sorted array.

Time Complexity: O(n * alpha(n)) — n union/find operations with path
                  halving and union by size
Space Complexity: O(n) — parent and size arrays
"""


# ----------------------------- Solution ----------------------------------


import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]

def solve():
    input = sys.stdin.readline
    n = int(input())
    p = list(map(int, input().split()))
    d = list(map(int, input().split()))
    dsu = DSU(n)
    for i in range(n):
        if i - d[i] >= 0:
            dsu.union(i, i - d[i])
        if i + d[i] < n:
            dsu.union(i, i + d[i])
    for i in range(n):
        original_pos = p[i] - 1
        if dsu.find(i) != dsu.find(original_pos):
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    solve()
