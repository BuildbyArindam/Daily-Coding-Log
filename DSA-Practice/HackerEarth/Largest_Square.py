"""
Problem   : Largest Square
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/largest-square-3d7a938a/
Difficulty: Medium
Topics    : Arrays, Data Structures, Multi-dimensional
Date      : 2026-09-24

Approach:
    Store all points in a hash set for O(1) lookup and group x-coordinates by
    their y-value (sorted). For every pair of points on the same horizontal
    line (x1, y) and (x2, y), the side is x2 - x1. The square exists if the
    two corners (x1, y + side) and (x2, y + side) are also in the set.
    Track the largest side, breaking ties by smaller y, then smaller x1.
    Print the bottom-left corner of the best square, or -1 if none exists.

Complexity:
    Time  : O(sum of m_y^2) over all rows, where m_y is the number of points
            on row y. Worst case O(N^2) when all points share one row.
    Space : O(N) for the point set and row groupings.
"""


# ------------------------------------------ Solution -----------------------------------------------------


import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
points = set()
rows = defaultdict(list)
for _ in range(N):
    x, y = map(int, input().split())
    points.add((x, y))
    rows[y].append(x)
for y in rows:
    rows[y].sort()
best_side = -1
best_x = -1
best_y = -1
for y, xs in rows.items():
    m = len(xs)
    for i in range(m):
        x1 = xs[i]
        for j in range(i + 1, m):
            x2 = xs[j]
            side = x2 - x1
            if side == 0:
                continue
            if (x1, y + side) in points and (x2, y + side) in points:
                if (
                    side > best_side
                    or (side == best_side and y < best_y)
                    or (side == best_side and y == best_y and x1 < best_x)
                ):
                    best_side = side
                    best_x = x1
                    best_y = y
if best_side == -1:
    print(-1)
else:
    print(best_x, best_y)
