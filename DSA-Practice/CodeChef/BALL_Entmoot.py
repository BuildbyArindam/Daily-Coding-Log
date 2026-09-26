"""
Problem   : Entmoot
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/icpc/ICPCTR07/problems/BALL
Date      : 2026-09-26
Difficulty: Hard
Topics    : Ternary search on convex functions, nested/2D ternary search,
            computational geometry (weighted smallest enclosing circle)

Approach:
  For each Ent, the "danger" at a candidate point (px, py) scales as
  ((px-x_i)^2 + (py-y_i)^2) / s_i^2. We want the point minimizing the
  worst-case (max) danger over all Ents — this is a weighted 1-center
  problem. The max of convex functions is convex, so the objective is
  convex in (px, py). We exploit this with a nested ternary search:
  an outer ternary search over px, and for each px an inner ternary
  search over py to compute the minimum achievable cost at that px.
  60 iterations each give ~1e-18 relative precision on the search
  interval, comfortably beating typical 1e-6 tolerance.
  Answer is sqrt of the minimized worst-case squared/scaled distance.

Complexity:
  Time : O(T * ITERS_x * ITERS_y * N) = O(T * 60 * 60 * N)
  Space: O(N) per test case
"""


# --------------------------------------------- Solution ----------------------------------------


import sys
import math

def answer(points):
    n = len(points)
    lx = min(p[0] for p in points)
    rx = max(p[0] for p in points)
    ly = min(p[1] for p in points)
    ry = max(p[1] for p in points)
    xx = [p[0] for p in points]
    yy = [p[1] for p in points]
    inv_s2 = [1.0 / (p[2] * p[2]) for p in points]
    def cost(px, py):
        worst = 0.0
        for i in range(n):
            dx = px - xx[i]
            dy = py - yy[i]
            cur = (dx * dx + dy * dy) * inv_s2[i]
            if cur > worst:
                worst = cur
        return worst
    def optimize_y(px):
        a = ly
        b = ry
        for _ in range(60):
            m1 = a + (b - a) / 3.0
            m2 = b - (b - a) / 3.0
            if cost(px, m1) <= cost(px, m2):
                b = m2
            else:
                a = m1
        return cost(px, (a + b) * 0.5)
    a = lx
    b = rx
    for _ in range(60):
        m1 = a + (b - a) / 3.0
        m2 = b - (b - a) / 3.0
        if optimize_y(m1) <= optimize_y(m2):
            b = m2
        else:
            a = m1
    best_x = (a + b) * 0.5
    return math.sqrt(optimize_y(best_x))

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = 0
    t = int(data[k])
    k += 1
    output = []
    for _ in range(t):
        n = int(data[k])
        k += 1
        ents = []
        for _ in range(n):
            x = int(data[k])
            y = int(data[k + 1])
            s = int(data[k + 2])
            k += 3
            ents.append((x, y, s))
        output.append(f"{answer(ents):.6f}")
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
