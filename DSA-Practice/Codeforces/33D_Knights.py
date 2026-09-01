"""
Problem: Knights
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/33/D
Date: 2026-09-01
Difficulty: *2000
Topics: Geometry, Graphs, Shortest Paths, Sortings

Approach:
    For each of the m circles, precompute a bitmask per point marking whether
    that point lies strictly inside the circle (bit j set = point is inside
    circle j). Two points are "fence-separated" by circle j exactly when they
    differ on bit j, so XOR-ing the two masks and popcounting the result gives
    the number of circular fences that must be crossed to travel between them
    — this equals the minimum number of circle-boundary crossings needed.

Complexity:
    Time:  O(n*m) to build masks, O(m/64) per query -> O(n*m + k*m/64) overall
    Space: O(n) for the masks array, O(1) extra per query
"""


# -------------------------- Solution ---------------------------------


import sys

def solve():
    input = sys.stdin.buffer.readline
    n, m, k = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    circles = [tuple(map(int, input().split())) for _ in range(m)]
    masks = [0] * n
    for j, (r, cx, cy) in enumerate(circles):
        rr = r * r
        bit = 1 << j
        for i, (x, y) in enumerate(points):
            dx = x - cx
            dy = y - cy
            if dx * dx + dy * dy < rr:
                masks[i] |= bit
    out = []
    for _ in range(k):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        answer = (masks[a] ^ masks[b]).bit_count()
        out.append(str(answer))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
