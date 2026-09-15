"""
Problem   : Reach the Destination
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380920
Difficulty: Easy
Date      : 2026-09-15
Topic     : Math, Number Theory (GCD)

Approach:
    Work backward from (dx, dy) to (sx, sy) using the Euclidean
    algorithm — repeatedly reduce the larger coordinate modulo the
    smaller one, mirroring how (sx, sy) could have been transformed
    into (dx, dy) via the allowed moves. Once one coordinate matches
    its source value, check that the remaining difference along the
    other axis is a multiple of the fixed coordinate.

Time complexity : O(log(min(dx, dy)))  — same bound as the Euclidean algorithm
Space complexity: O(1)
"""


# ------------------------------- Solution ------------------------------------


def reachDestination(sx,sy,dx,dy):
    if dx < sx or dy < sy:
        return False
    while dx > sx and dy > sy:
        if dx > dy:
            dx %= dy
        else:
            dy %= dx
    if dx == sx and dy >= sy:
        return (dy - sy) % sx == 0
    if dy == sy and dx >= sx:
        return (dx - sx) % sy == 0
    return False
