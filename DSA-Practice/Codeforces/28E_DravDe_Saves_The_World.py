"""
Problem   : DravDe saves the world
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/28/E
Difficulty: *2800
Topics    : Geometry, Math
Date      : 2026-08-29

Approach:
    Model the problem in the moving reference frame of the "danger zone"
    polygon. Two independent scan speeds (vx,vy) and (ux,uy) define a
    linear map from time (t, t2) to displacement; when this map is
    non-degenerate (D = cross(v,u) != 0), each polygon edge is clipped
    against the two half-plane constraints derived from the swept
    directions, reducing the search to the feasible parameter interval
    [lo, hi] per edge. The best (t, r) pair (minimal t, then maximal r
    as tiebreak) is tracked across all edges, then mapped back to the
    original (t, t2) time coordinates via t2 = (-zu*r - zv*t) / fdown.
    When D == 0 (degenerate/parallel case), the scan direction collapses
    to a single line, so intersections with polygon edges are found via
    a 1D projection (cross product == 0 crossing) instead, and the
    closest positive/negative intersection along that line determines
    the answer.

Complexity:
    Time : O(n) per case — single pass over polygon edges (n <= 1000)
    Space: O(n) — storing the polygon vertices
"""


# ----------------------------- Solution ---------------------------------------


import sys

def cross(ax, ay, bx, by):
    return ax * by - ay * bx
def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    n = next(it)
    poly = [(next(it), next(it)) for _ in range(n)]
    xa, ya = next(it), next(it)
    vx, vy, zv = next(it), next(it), next(it)
    fdown = next(it)
    ux, uy, zu = next(it), next(it), next(it)
    alpha = zv / (-zu)
    D = vx * uy - vy * ux
    EPS = 1e-10
    if D != 0:
        bx = (-zu) * vx + zv * ux
        by = (-zu) * vy + zv * uy
        sign = 1 if D > 0 else -1
        best_t = None
        best_r = None
        for i in range(n):
            p0 = poly[i]
            p1 = poly[(i + 1) % n]
            x0 = p0[0] - xa
            y0 = p0[1] - ya
            x1 = p1[0] - xa
            y1 = p1[1] - ya
            f10 = sign * cross(vx, vy, x0, y0)
            f11 = sign * cross(vx, vy, x1, y1)
            f20 = -sign * cross(bx, by, x0, y0)
            f21 = -sign * cross(bx, by, x1, y1)
            lo = 0.0
            hi = 1.0
            feasible = True
            for f0, f1 in ((f10, f11), (f20, f21)):
                if f0 < 0 and f1 < 0:
                    feasible = False
                    break
                if f0 < 0:
                    s = (-f0) / (f1 - f0)
                    if s > lo:
                        lo = s
                elif f1 < 0:
                    s = f0 / (f0 - f1)
                    if s < hi:
                        hi = s
            if not feasible or lo > hi + EPS:
                continue
            lo = max(0.0, min(1.0, lo))
            hi = max(0.0, min(1.0, hi))
            t0 = cross(x0, y0, ux, uy) / D
            t1 = cross(x1, y1, ux, uy) / D
            r0 = cross(vx, vy, x0, y0) / D
            r1 = cross(vx, vy, x1, y1) / D
            dt = t1 - t0
            dr = r1 - r0
            for s in (lo, hi):
                t = t0 + dt * s
                r = r0 + dr * s
                if t < -1e-8:
                    continue
                if t < 0:
                    t = 0.0
                scale = max(
                    1.0,
                    abs(t),
                    abs(best_t) if best_t is not None else 1.0
                )
                if best_t is None or t < best_t - EPS * scale:
                    best_t = t
                    best_r = r
                elif abs(t - best_t) <= EPS * scale:
                    if r > best_r:
                        best_r = r
        if best_t is None:
            print("-1 -1")
            return
        t2 = (-zu * best_r - zv * best_t) / fdown
        if abs(t2) < 5e-10:
            t2 = 0.0
        print(f"{best_t:.10f} {t2:.10f}")
        return
    if vx != 0 or vy != 0:
        wx, wy = vx, vy
        a = 1.0
        denom = vx * vx + vy * vy
        b = (ux * vx + uy * vy) / denom
    elif ux != 0 or uy != 0:
        wx, wy = ux, uy
        a = 0.0
        b = 1.0
    else:
        print("-1 -1")
        return
    wlen2 = wx * wx + wy * wy
    closest_positive = None
    closest_negative = None
    for i in range(n):
        p0 = poly[i]
        p1 = poly[(i + 1) % n]
        x0 = p0[0] - xa
        y0 = p0[1] - ya
        x1 = p1[0] - xa
        y1 = p1[1] - ya
        g0 = cross(wx, wy, x0, y0)
        g1 = cross(wx, wy, x1, y1)
        c0 = (x0 * wx + y0 * wy) / wlen2
        c1 = (x1 * wx + y1 * wy) / wlen2
        intersections = []
        if g0 == 0 and g1 == 0:
            intersections = [c0, c1]
        elif g0 == 0:
            intersections = [c0]
        elif g1 == 0:
            intersections = [c1]
        elif (g0 > 0) != (g1 > 0):
            s = g0 / (g0 - g1)
            c = c0 + (c1 - c0) * s
            intersections = [c]
        for c in intersections:
            if c > 1e-12:
                if closest_positive is None or c < closest_positive:
                    closest_positive = c
            elif c < -1e-12:
                if closest_negative is None or c > closest_negative:
                    closest_negative = c
    h0 = a
    h1 = a + b * alpha
    best_t = None
    best_r = None
    def consider(c, positive):
        nonlocal best_t, best_r
        if positive:
            hs = [h for h in (h0, h1) if h > 1e-14]
            if not hs:
                return
            h = max(hs)
        else:
            hs = [h for h in (h0, h1) if h < -1e-14]
            if not hs:
                return
            h = min(hs)
        t = c / h
        if t <= 0:
            return
        if abs(b) < 1e-14:
            q = alpha
        else:
            q = (h - a) / b
            q = max(0.0, min(alpha, q))
        r = q * t
        scale = max(
            1.0,
            abs(t),
            abs(best_t) if best_t is not None else 1.0
        )
        if best_t is None or t < best_t - EPS * scale:
            best_t = t
            best_r = r
        elif abs(t - best_t) <= EPS * scale and r > best_r:
            best_r = r
    if closest_positive is not None:
        consider(closest_positive, True)
    if closest_negative is not None:
        consider(closest_negative, False)
    if best_t is None:
        print("-1 -1")
        return
    t2 = (-zu * best_r - zv * best_t) / fdown
    if abs(t2) < 5e-10:
        t2 = 0.0
    print(f"{best_t:.10f} {t2:.10f}")

if __name__ == "__main__":
    solve()
