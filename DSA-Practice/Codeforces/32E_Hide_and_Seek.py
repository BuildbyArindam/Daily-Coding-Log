"""
Problem: Hide-and-Seek
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/32/E
Difficulty: *2400
Date Solved: 2026-09-01
Topics: Geometry, Implementation

Approach:
Two visibility checks between Victor and Peter — direct line of sight
(blocked by the wall, and by the mirror unless VP is parallel to it),
and mirrored line of sight (Victor and Peter on the same side of the
mirror line; reflect Peter across the mirror, intersect V-P_reflected
with the mirror segment, and require both resulting sub-segments to
avoid the wall). All geometry (cross product, segment intersection,
reflection, line intersection) done with exact Fraction arithmetic to
avoid floating-point precision errors.

Time Complexity:  O(1) — constant number of geometric primitive calls
Space Complexity: O(1)
"""


# ------------------------ Solution --------------------------------


from fractions import Fraction


def cross(a, b, c):
    """Cross product of AB and AC."""
    return (b[0] - a[0]) * (c[1] - a[1]) - \
           (b[1] - a[1]) * (c[0] - a[0])


def on_segment(a, b, p):
    """Whether p lies on the closed segment AB."""
    return (
        cross(a, b, p) == 0
        and min(a[0], b[0]) <= p[0] <= max(a[0], b[0])
        and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
    )

def segments_intersect(a, b, c, d):
    """Whether closed segments AB and CD have a common point."""
    c1 = cross(a, b, c)
    c2 = cross(a, b, d)
    c3 = cross(c, d, a)
    c4 = cross(c, d, b)
    if ((c1 > 0 and c2 < 0) or (c1 < 0 and c2 > 0)) and \
       ((c3 > 0 and c4 < 0) or (c3 < 0 and c4 > 0)):
        return True
    return (
        (c1 == 0 and on_segment(a, b, c)) or
        (c2 == 0 and on_segment(a, b, d)) or
        (c3 == 0 and on_segment(c, d, a)) or
        (c4 == 0 and on_segment(c, d, b))
    )

def reflect_point(p, a, b):
    """
    Reflect point p across the infinite line through a and b.
    Returns exact Fraction coordinates.
    """
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    cr = dx * (p[1] - a[1]) - dy * (p[0] - a[0])
    den = dx * dx + dy * dy
    rx = p[0] + Fraction(2 * cr * dy, den)
    ry = p[1] - Fraction(2 * cr * dx, den)
    return rx, ry

def line_intersection(p, q, a, b):
    """
    Intersection of lines PQ and AB.
    Returns the intersection point as Fractions.
    """
    rx = q[0] - p[0]
    ry = q[1] - p[1]
    sx = b[0] - a[0]
    sy = b[1] - a[1]
    den = rx * sy - ry * sx
    if den == 0:
        return None 
    apx = a[0] - p[0]
    apy = a[1] - p[1]
    t = Fraction(apx * sy - apy * sx, den)
    return p[0] + t * rx, p[1] + t * ry

def can_see(V, P, W1, W2, M1, M2):
    mirror_dx = M2[0] - M1[0]
    mirror_dy = M2[1] - M1[1]
    vp_dx = P[0] - V[0]
    vp_dy = P[1] - V[1]
    parallel = mirror_dx * vp_dy - mirror_dy * vp_dx == 0
    mirror_allows_direct = (
        parallel or not segments_intersect(V, P, M1, M2)
    )
    wall_allows_direct = not segments_intersect(V, P, W1, W2)
    if mirror_allows_direct and wall_allows_direct:
        return True
    side_v = cross(M1, M2, V)
    side_p = cross(M1, M2, P)
    if side_v * side_p <= 0:
        return False
    P_ref = reflect_point(P, M1, M2)
    I = line_intersection(V, P_ref, M1, M2)
    if I is None:
        return False
    if not on_segment(M1, M2, I):
        return False
    if segments_intersect(V, I, W1, W2):
        return False
    if segments_intersect(I, P, W1, W2):
        return False
    return True

def main():
    xv, yv = map(int, input().split())
    xp, yp = map(int, input().split())
    xw1, yw1, xw2, yw2 = map(int, input().split())
    xm1, ym1, xm2, ym2 = map(int, input().split())
    V = (Fraction(xv), Fraction(yv))
    P = (Fraction(xp), Fraction(yp))
    W1 = (Fraction(xw1), Fraction(yw1))
    W2 = (Fraction(xw2), Fraction(yw2))
    M1 = (Fraction(xm1), Fraction(ym1))
    M2 = (Fraction(xm2), Fraction(ym2))
    print("YES" if can_see(V, P, W1, W2, M1, M2) else "NO")

if __name__ == "__main__":
    main()
