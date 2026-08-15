"""
Problem   : A Colourful Prospect
Platform  : Codeforces
Link      : https://codeforces.com/contest/934/problem/E
Rating    : *2700
Topics    : Geometry, Graph Theory (Planar Graphs / Euler's Formula)
Date      : 2026-08-15

Approach:
    Given up to 3 circles, count the number of regions (faces) they divide
    the plane into. Treat the union of circle boundaries as a planar graph:
    - Vertices (V): pairwise circle intersection points (dedup via EPS
      comparison), plus one synthetic "leftmost point" per circle to anchor
      circles that don't intersect anyone.
    - Edges (E): each circle contributes (number of distinct points on it)
      arcs; a circle with k marked points splits into k arcs (or 1 full
      loop if isolated).
    - Connected Components (C): tracked via a union-like counter (`add[]`)
      over which pairs of circles actually intersect, to know how many
      disjoint "clusters" of circles exist.
    - Faces (F) via Euler's formula for planar graphs: V - E + F = 1 + C
      (the "+1" accounts for the outer unbounded face), rearranged to
      solve for F = E - V + C + 1, which is the final answer (regions,
      including the unbounded outer region).
    n == 1 and n == 2 are handled as direct closed-form special cases
    (2 regions for a single circle; 3 or 4 depending on intersection type
    for two circles) since Euler's formula edge cases get fiddly there.

Complexity:
    Time  : O(1) — n <= 3 circles fixed, so all intersection checks (O(n^2))
            and point dedup are bounded by small constants (<= 3 pairs,
            <= ~8 points per circle).
    Space : O(1) — fixed-size point lists per circle.
"""


# ------------------------- Solution ------------------------- 


import sys
import math

EPS = 1e-8

def dcmp(x):
    if x > EPS:
        return 1
    if x < -EPS:
        return -1
    return 0

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return (
            dcmp(self.x - other.x) == 0
            and dcmp(self.y - other.y) == 0
        )

n = int(input())
a = [Point() for _ in range(5)]
r = [0.0] * 5
for i in range(1, n + 1):
    x, y, radius = map(float, input().split())
    a[i] = Point(x, y)
    r[i] = radius
in1 = Point()
in2 = Point()
def get_inter(c1, r1, c2, r2):
    global in1, in2
    A = 2.0 * (c2.x - c1.x)
    B = 2.0 * (c2.y - c1.y)
    C = (
        c1.x * c1.x
        + c1.y * c1.y
        - c2.x * c2.x
        - c2.y * c2.y
        - r1 * r1
        + r2 * r2
    )
    # Same center: no intersection unless circles are identical.
    # Identical circles are forbidden by the statement.
    if dcmp(A) == 0 and dcmp(B) == 0:
        return 0
    dist_to_line = abs(A * c1.x + B * c1.y + C) / math.sqrt(A * A + B * B)
    res = dcmp(dist_to_line - r1)
    if res <= 0:
        if dcmp(A) == 0:
            # A = 0, so B != 0
            y = -C / B
            t = r1 * r1 - (y - c1.y) * (y - c1.y)
            if dcmp(t):
                t = math.sqrt(t)
            else:
                t = 0.0
            in1.x = c1.x - t
            in1.y = y
            in2.x = c1.x + t
            in2.y = y
        else:
            k = B / A
            tA = k * k + 1.0
            tB = 2.0 * (k * (C / A + c1.x) - c1.y)
            tC = (
                (C / A + c1.x) * (C / A + c1.x)
                + c1.y * c1.y
                - r1 * r1
            )
            delta = tB * tB - 4.0 * tA * tC
            if dcmp(delta):
                delta = math.sqrt(delta)
            else:
                delta = 0.0
            in1.y = (-tB - delta) / (2.0 * tA)
            in1.x = -(B * in1.y + C) / A
            in2.y = (-tB + delta) / (2.0 * tA)
            in2.x = -(B * in2.y + C) / A
        if res < 0:
            return 2
        else:
            return 1
    return 0
pt = [[] for _ in range(5)]
def insert(idx, p):
    for q in pt[idx]:
        if p == q:
            return
    pt[idx].append(Point(p.x, p.y))
if n == 1:
    print(2)
    sys.exit()
if n == 2:
    t = get_inter(a[1], r[1], a[2], r[2])
    print(4 if t == 2 else 3)
    sys.exit()
for i in range(1, 4):
    p = Point(a[i].x - r[i], a[i].y)
    insert(i, p)
    insert(0, p)
add = [1, 1, 1, 1, 1]
for i in range(1, 4):
    for j in range(i + 1, 4):
        t = get_inter(a[i], r[i], a[j], r[j])
        if t == 2:
            insert(i, in1)
            insert(i, in2)
            insert(j, in1)
            insert(j, in2)
            insert(0, in1)
            insert(0, in2)
        elif t == 1:
            insert(i, in1)
            insert(j, in1)
            insert(0, in1)
        else:
            add[i ^ j] = 0
t = add[1] + add[2] + add[3]
if t >= 2:
    t = 1
elif t == 1:
    t = 2
else:
    t = 3
ans = len(pt[1]) + len(pt[2]) + len(pt[3]) - len(pt[0]) + t + 1
print(ans)
