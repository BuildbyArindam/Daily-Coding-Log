"""
Problem   : Plant Location (K1)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/K1
Difficulty: 1802
Date      : 2026-10-04
Topics    : Computational Geometry, Ternary Search, Lines, Mathematics

Approach:
    Place a plant on the line Ax + By + C = 0 so that the sum of Euclidean
    distances to all N points is minimal.
    1. Rotate into line-aligned coordinates: for each point, s is its
       position along the line and h is its signed perpendicular distance.
    2. A plant at position p on the line is at distance sqrt((p - s)^2 + h^2)
       from the point, so the total cost f(p) is a sum of convex functions
       and therefore convex.
    3. Find the minimum of f(p) by binary search on its derivative
       (equivalent to ternary search, but converges faster per iteration):
       f'(p) = sum((p - s) / sqrt((p - s)^2 + h^2)).
       The optimum lies within [min(s), max(s)].

Complexity:
    Time : O(T * N * I), where I = 100 iterations
    Space: O(N)
"""


# --------------------------------------------- Solution -------------------------------------------------


import sys
import math

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A, B, C = map(int, input().split())
        norm = math.hypot(A, B)
        positions = []
        heights = []
        for _ in range(N):
            x, y = map(int, input().split())
            s = (B * x - A * y) / norm
            h = (A * x + B * y + C) / norm
            positions.append(s)
            heights.append(h)
        lo = min(positions)
        hi = max(positions)
        for _ in range(100):
            mid = (lo + hi) / 2.0
            derivative = 0.0
            for s, h in zip(positions, heights):
                dx = mid - s
                derivative += dx / math.hypot(dx, h)
            if derivative < 0:
                lo = mid
            else:
                hi = mid
        p = (lo + hi) / 2.0
        answer = 0.0
        for s, h in zip(positions, heights):
            answer += math.hypot(p - s, h)
        print(f"{answer:.6f}")

if __name__ == "__main__":
    solve()
