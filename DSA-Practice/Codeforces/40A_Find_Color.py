"""
Problem   : Find Color (Codeforces 40A)
Link      : https://codeforces.com/problemset/problem/40/A
Date      : 2026-09-07
Topic     : Constructive Algorithms, Geometry, Implementation, Math

Approach:
Cells are colored like a checkerboard on concentric square "rings" around
the origin. For a point (x, y):
  1. Compute d = x^2 + y^2 (squared distance from origin).
  2. r = ceil(sqrt(d)) is the ring index the point lies on (isqrt + fix-up
     if d isn't a perfect square).
  3. If d is a perfect square, the point sits exactly on a ring boundary
     -> always "black".
  4. Otherwise, color alternates by ring parity, but flips again depending
     on which quadrant (sign of x*y) the point is in — this matches how
     the checkerboard flips across the axes.

Complexity: O(1) time, O(1) space (single isqrt call, no loops).
"""


# --------------------------- Solution ---------------------------------


import math
x, y = map(int, input().split())
d = x * x + y * y
r = math.isqrt(d)
if r * r == d:
    print("black")
else:
    r += 1
    if (r % 2 == 1) == (x * y > 0):
        print("black")
    else:
        print("white")
