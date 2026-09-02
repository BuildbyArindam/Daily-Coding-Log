"""
Problem   : Fire Again
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/35/C
Difficulty: 1500
Topics    : Brute Force, DFS and Similar, Shortest Paths
Date      : 2026-09-02

Approach:
    Binary search on the answer distance `d` (the max possible minimum
    Chebyshev distance from the chosen tree to any fire). For a candidate
    `d`, a tree is "safe" if it lies outside every fire's diamond of
    radius d-1 (Chebyshev ball). For each row x, compute the union of
    "burnt" y-intervals contributed by fires within reach of that row,
    then look for a gap (uncovered y) in [1, M]. If a gap exists for
    some row, `d` is feasible -> search higher; otherwise search lower.
    The largest feasible `d` gives the answer point.

Complexity:
    Let d(N, M) = number of binary search steps ~ O(log(N+M)).
    Each feasibility check (find_point) scans all N rows and, for each
    row, filters and sorts up to K fire-intervals.
        Time : O(N * K log K * log(N+M))
        Space: O(K) per feasibility check (interval list)
"""


# ------------------------ Solution ----------------------------


import os
import sys

if os.path.exists("input.txt"):
    with open("input.txt", "rb") as f:
        data = list(map(int, f.read().split()))
    use_files = True
else:
    data = list(map(int, sys.stdin.buffer.read().split()))
    use_files = False
p = 0
N = data[p]
M = data[p + 1]
p += 2
K = data[p]
p += 1
fires = []
for _ in range(K):
    x = data[p]
    y = data[p + 1]
    p += 2
    fires.append((x, y))

def find_point(d):
    """
    Return a point whose distance from every initial fire is >= d.
    Return None if no such point exists.
    """
    # Trees with distance < d are inside a diamond of radius d - 1.
    r = d - 1
    for x in range(1, N + 1):
        intervals = []
        for fx, fy in fires:
            dx = abs(x - fx)
            if dx <= r:
                remaining = r - dx
                left = max(1, fy - remaining)
                right = min(M, fy + remaining)
                if left <= right:
                    intervals.append((left, right))
        if not intervals:
            return x, 1
        intervals.sort()
        left, right = intervals[0]
        if left > 1:
            return x, 1
        for l, rr in intervals[1:]:
            if l > right + 1:
                return x, right + 1
            if rr > right:
                right = rr
        if right < M:
            return x, right + 1
    return None
lo = 0
hi = N + M
while lo < hi:
    mid = (lo + hi + 1) // 2
    if find_point(mid) is not None:
        lo = mid
    else:
        hi = mid - 1
answer = find_point(lo)
result = f"{answer[0]} {answer[1]}\n"
if use_files:
    with open("output.txt", "w") as f:
        f.write(result)
else:
    sys.stdout.write(result)
