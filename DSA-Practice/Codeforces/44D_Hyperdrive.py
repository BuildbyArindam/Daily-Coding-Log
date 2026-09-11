"""
Problem: Hyperdrive
Link: http://codeforces.com/problemset/problem/44/D
Platform: Codeforces
Date solved: 2026-09-11
Difficulty: *1800
Topic: Math (geometry / distance minimization)

Approach:
The message spreads outward from planet 1 in straight lines. The total time
for every planet to receive it is fixed by the last two planets it reaches,
which meet via the shortest "1 -> i -> j" or "1 -> j -> i" relay path. So the
answer is min over pairs (i, j) of (dist(1,i) + dist(1,j) + dist(i,j)) / 2.
Planets are sorted by distance from planet 1 so that once 2*r_i (or 2*r_j)
exceeds the current best, no further pair starting there can improve it,
letting the search break out early instead of checking all O(n^2) pairs.

Time complexity:  O(n log n) for the sort; O(n^2) worst case for the pair
                   search, but pruning makes it run well within limits in
                   practice for the given constraints.
Space complexity: O(n) for storing planet distances/coordinates.
"""


# --------------------------- Solution ---------------------------------


import sys
import math

def solve():
    input = sys.stdin.readline
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    x0, y0, z0 = points[0]
    planets = []
    for x, y, z in points[1:]:
        dx = x - x0
        dy = y - y0
        dz = z - z0
        d = math.sqrt(dx * dx + dy * dy + dz * dz)
        planets.append((d, x, y, z))
    planets.sort()
    r1, x1, y1, z1 = planets[0]
    r2, x2, y2, z2 = planets[1]
    dx = x1 - x2
    dy = y1 - y2
    dz = z1 - z2
    best = r1 + r2 + math.sqrt(dx * dx + dy * dy + dz * dz)
    m = len(planets)
    for i in range(m - 1):
        ri, xi, yi, zi = planets[i]
        if 2.0 * ri >= best:
            break
        for j in range(i + 1, m):
            rj, xj, yj, zj = planets[j]
            if 2.0 * rj >= best:
                break
            dx = xi - xj
            dy = yi - yj
            dz = zi - zj
            d = math.sqrt(dx * dx + dy * dy + dz * dz)
            perimeter = ri + rj + d
            if perimeter < best:
                best = perimeter
    print("{:.10f}".format(best / 2.0))

if __name__ == "__main__":
    solve()
