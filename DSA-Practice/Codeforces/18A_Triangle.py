"""
Problem: Triangle
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/18/A
Date Solved: 2026-08-24
Difficulty: *1500
Topics: Brute Force, Geometry

Approach:
Check if the given triangle is already right-angled using the
Pythagorean relation on squared side lengths (avoids floating point
issues). If not, try nudging each of the 3 points by 1 unit in each
of the 4 cardinal directions (12 total perturbations) and re-check
after each move — if any perturbation makes it right-angled, it's
"ALMOST". Otherwise "NEITHER". Degenerate (collinear) triangles are
excluded via the twice-area check.

Time Complexity:  O(1) — constant number of checks (13 total: 1 original + 12 perturbations)
Space Complexity: O(1) — fixed-size point list
"""


# ------------------------ Solution ------------------------------

import sys

def is_right(p1, p2, p3):
    area2 = (
        p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])
    )
    if area2 == 0:
        return False
    d12 = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    d23 = (p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2
    d31 = (p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2
    return (
        (d12 + d23 == d31) or (d12 + d31 == d23) or (d23 + d31 == d12)
    )

def solve():
    coords = list(map(int, sys.stdin.read().split()))
    if not coords:
        return
    p1 = [coords[0], coords[1]]
    p2 = [coords[2], coords[3]]
    p3 = [coords[4], coords[5]]
    if is_right(p1, p2, p3):
        print("RIGHT")
        return
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    points = [p1, p2, p3]
    for i in range(3):
        original = points[i][:]
        for dx, dy in moves:
            points[i] = [original[0] + dx, original[1] + dy]
            if is_right(points[0], points[1], points[2]):
                print("ALMOST")
                return
        points[i] = original
    print("NEITHER")

if __name__ == "__main__":
    solve()
