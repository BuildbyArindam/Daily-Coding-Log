"""
Problem   : Shooting Gallery
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/44/G
Difficulty: *2500
Topics    : Data Structures, Implementation
Date      : 2026-09-11

Approach:
    Offline processing of targets in increasing order of z (nearest
    first), each target claiming the smallest-indexed active shot
    that falls inside its rectangle [xl, xr] x [yl, yr].

    A static KD-tree is built once over all m shots (points), where
    each node stores the bounding box of its subtree plus `mn`, the
    smallest active (undeleted) shot id in that subtree. Deleting a
    shot only updates `mn` values on the path to the root — the
    geometric bounding boxes never change, so no rebuild is needed.

    For each target (processed by increasing z):
        - query() walks the KD-tree, pruning subtrees whose bounding
          box doesn't intersect the query rectangle or whose `mn`
          can't beat the current best, and short-circuits whenever a
          subtree lies entirely inside the rectangle.
        - If a shot is found, it's assigned to that target and
          erase() marks it inactive, propagating the new `mn` values
          upward.

Complexity:
    Build      : O(m log m)
    Query/Erase: O(sqrt(m)) amortized per query on a 2D KD-tree,
                 O(log m) for erase.
    Overall    : O((n + m) sqrt(m))  time
                 O(n + m)            space
"""


# ----------------------------- Solution -------------------------------------


import sys
from operator import itemgetter
sys.setrecursionlimit(1_000_000)
INF = 10**9

def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    targets = []
    for target_id in range(1, n + 1):
        xl, xr, yl, yr, z = map(int, input().split())
        targets.append((z, xl, yl, xr, yr, target_id))
    m = int(input())
    points = []
    for shot_id in range(m):
        x, y = map(int, input().split())
        points.append((x, y, shot_id))
    targets.sort(key=itemgetter(0))
    size = 4 * m + 5
    min_x = [0] * size
    max_x = [0] * size
    min_y = [0] * size
    max_y = [0] * size
    mn = [INF] * size
    pos = [0] * m
    get_x = itemgetter(0)
    get_y = itemgetter(1)
    def build(l, r, u, depth):
        if l == r:
            x, y, shot = points[l]
            min_x[u] = max_x[u] = x
            min_y[u] = max_y[u] = y
            mn[u] = shot
            pos[shot] = u
            return
        if depth == 0:
            points[l:r + 1] = sorted(points[l:r + 1], key=get_x)
        else:
            points[l:r + 1] = sorted(points[l:r + 1], key=get_y)
        mid = (l + r) >> 1
        left = u << 1
        right = left | 1
        build(l, mid, left, depth ^ 1)
        build(mid + 1, r, right, depth ^ 1)
        min_x[u] = min_x[left] if min_x[left] < min_x[right] else min_x[right]
        max_x[u] = max_x[left] if max_x[left] > max_x[right] else max_x[right]
        min_y[u] = min_y[left] if min_y[left] < min_y[right] else min_y[right]
        max_y[u] = max_y[left] if max_y[left] > max_y[right] else max_y[right]
        mn[u] = mn[left] if mn[left] < mn[right] else mn[right]
    build(0, m - 1, 1, 0)
    def query(xl, yl, xr, yr):
        best = INF
        stack = [1]
        while stack:
            u = stack.pop()
            if mn[u] >= best:
                continue
            if (
                max_x[u] < xl or
                min_x[u] > xr or
                max_y[u] < yl or
                min_y[u] > yr
            ):
                continue
            if (
                xl <= min_x[u] and
                max_x[u] <= xr and
                yl <= min_y[u] and
                max_y[u] <= yr
            ):
                best = mn[u]
                continue
            left = u << 1
            right = left | 1
            if mn[left] < mn[right]:
                if mn[right] < best:
                    stack.append(right)
                if mn[left] < best:
                    stack.append(left)
            else:
                if mn[left] < best:
                    stack.append(left)
                if mn[right] < best:
                    stack.append(right)
        return best
    def erase(shot):
        u = pos[shot]
        mn[u] = INF
        u >>= 1
        while u:
            left = u << 1
            right = left | 1
            mn[u] = mn[left] if mn[left] < mn[right] else mn[right]
            u >>= 1
    answer = [0] * m
    for z, xl, yl, xr, yr, target_id in targets:
        shot = query(xl, yl, xr, yr)
        if shot != INF:
            answer[shot] = target_id
            erase(shot)
    sys.stdout.write("\n".join(map(str, answer)))

if __name__ == "__main__":
    main()
