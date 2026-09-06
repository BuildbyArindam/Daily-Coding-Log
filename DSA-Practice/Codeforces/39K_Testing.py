"""
Problem   : 39K - Testing
Link      : https://codeforces.com/problemset/problem/39/K
Platform  : Codeforces
Difficulty: *2600
Topic     : Coordinate Compression / Sweep Line / Interval Merging / Combinatorics
Date      : 2026-09-06

Approach:
    - Identify the k rectangular objects on the grid by scanning for the
      top-left corner of each '*' block, then extending right/down to find
      its extent.
    - Compress the row axis to O(k) "critical" horizontal bands using the
      rows just below each object's top edge and each object's bottom edge,
      plus the grid boundaries. Any valid strike's top/bottom edges must
      fall on one of these critical lines, so iterating over pairs of them
      (top, bottom) covers all distinct vertical extents, weighted by how
      many original rows collapse into each band.
    - For a fixed vertical band [top, bottom), scan objects sorted by
      column and merge overlapping column-intervals into runs, tracking
      how many objects fall fully inside the vertical band (weight 1) vs.
      partially inside it (weight INF, since a valid strike can't cut an
      object in half). Runs with a combined weight in [1, 3] contribute
      valid horizontal extents; count the number of ways to place the
      left/right edges of the strike between the flanking merged runs.
    - Sum ways * vertical_weight_top * vertical_weight_bottom over all
      (top, bottom) critical-line pairs.

Complexity:
    Let s = O(k) be the number of critical rows (~2k+2).
    - Outer double loop over critical row pairs: O(s^2) = O(k^2)
    - Each count_x call: O(k log k) for sort + O(k) merge/scan
    - Total time : O(k^2 * k) = O(k^3) worst case (k <= 90, so ~7.3*10^5,
      trivially fast)
    - Extra grid parsing: O(n*m) to locate objects
    - Space      : O(n*m) for the grid, O(k) for objects/critical lines
"""


# ------------------------ Solution -------------------------------


import sys

def solve():
    input = sys.stdin.buffer.readline
    n, m, k = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    objects = []
    for r in range(n):
        for c in range(m):
            if grid[r][c] != ord('*'):
                continue
            if r > 0 and grid[r - 1][c] == ord('*'):
                continue
            if c > 0 and grid[r][c - 1] == ord('*'):
                continue
            right = c
            while right < m and grid[r][right] == ord('*'):
                right += 1
            bottom = r
            while bottom < n and grid[bottom][c] == ord('*'):
                bottom += 1
            objects.append((r, bottom, c, right))
    k = len(objects)
    critical = {0, n + 1}
    for t, b, l, r in objects:
        critical.add(t + 1)
        critical.add(b)
    critical = sorted(critical)
    reps = critical[:-1]
    weights = [
        critical[i + 1] - critical[i]
        for i in range(len(critical) - 1)
    ]
    INF = k + 1
    objects.sort(key=lambda x: x[2])
    def count_x(top, bottom):
        """
        Count possible x-intervals for a fixed vertical interval [top,bottom).
        Only rectangles hitting 1..3 objects are counted.
        """
        segs = []
        for t, b, l, r in objects:
            if b <= top or t >= bottom:
                continue
            if top <= t and b <= bottom:
                segs.append((l, r, 1))
            else:
                segs.append((l, r, INF))
        if not segs:
            return 0
        merged = []
        L, R, cnt = segs[0]
        for l, r, w in segs[1:]:
            if l < R:
                R = max(R, r)
                if cnt == INF or w == INF:
                    cnt = INF
                else:
                    cnt += w
            else:
                merged.append((L, R, cnt))
                L, R, cnt = l, r, w
        merged.append((L, R, cnt))
        q = len(merged)
        ans = 0
        for i in range(q):
            Li, Ri, ci = merged[i]
            if ci == INF or ci > 3:
                continue
            if i == 0:
                left_ways = Li + 1
            else:
                left_ways = Li - merged[i - 1][1] + 1
            total = 0
            for j in range(i, min(q, i + 3)):
                Lj, Rj, cj = merged[j]
                if cj == INF:
                    break
                total += cj
                if total > 3:
                    break
                if j + 1 == q:
                    right_ways = m - Rj + 1
                else:
                    right_ways = merged[j + 1][0] - Rj + 1
                ans += left_ways * right_ways
        return ans
    answer = 0
    s = len(reps)
    for i in range(s):
        top = reps[i]
        for j in range(i + 1, s):
            bottom = reps[j]
            ways = count_x(top, bottom)
            answer += ways * weights[i] * weights[j]
    print(answer)

if __name__ == "__main__":
    solve()
