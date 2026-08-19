"""
Problem   : Four Segments
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/14/C
Difficulty: *1700
Topics    : brute force, constructive algorithms, geometry, implementation, math
Date      : 2026-08-19

Approach:
Read 4 segments, classify each as horizontal (y1==y2, x1!=x2) or vertical
(x1==x2, y1!=y2). A valid axis-aligned rectangle of positive area requires
exactly 2 horizontal + 2 vertical segments, and the 8 endpoints must reduce
to exactly 4 unique points, each occurring exactly twice (so every corner
is shared by one horizontal and one vertical segment).

Note: this degree-based check is necessary but not fully sufficient — see
inline comment / commit notes for a duplicate-segment edge case.

Time complexity : O(1)  (fixed 4 segments, 8 endpoints)
Space complexity: O(1)
"""


# ----------------------- Solution ---------------------------


import sys

def solve():
    segments = []
    horiz = 0
    vert = 0
    endpoints = []
    for _ in range(4):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        segments.append((x1, y1, x2, y2))
        endpoints.append((x1, y1))
        endpoints.append((x2, y2))
        if y1 == y2 and x1 != x2:
            horiz += 1
        elif x1 == x2 and y1 != y2:
            vert += 1
    if horiz != 2 or vert != 2:
        print("NO")
        return
    unique_points = set(endpoints)
    if len(unique_points) != 4:
        print("NO")
        return
    for pt in unique_points:
        if endpoints.count(pt) != 2:
            print("NO")
            return
    print("YES")

if __name__ == '__main__':
    solve()
