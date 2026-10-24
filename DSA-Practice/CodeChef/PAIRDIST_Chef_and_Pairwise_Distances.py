"""
Platform   : CodeChef
Problem    : Chef and Pairwise Distances (PAIRDIST)
Link       : https://www.codechef.com/problems/PAIRDIST
Difficulty : 2012
Topics     : Constructive, Geometry
Date       : 2026-10-24

Approach:
    - If n > 4, print NO. The construction only supports at most 4 points.
    - Otherwise, sort the values in descending order. The largest value
      becomes the reference point at the origin.
    - Work in rotated coordinates (u, v) = (x + y, x - y), which turns
      Manhattan distance into Chebyshev distance. Place the remaining
      points at fixed offsets from the largest value:
          (big + s1, big - s1), (big - s2, big + s2), (big + s3, big + s3)
    - Convert back with x = (u + v) / 2 and y = (u - v) / 2, then restore
      the original input order via the saved index permutation.

Complexity:
    Time  : O(n log n) per test, effectively O(n) for reading input,
            since a case with n > 4 is rejected immediately.
    Space : O(n) for the input arrays and output buffer.
"""


# --------------------------------------- Solution ---------------------------------------------------------


import sys
def main():
    tok = sys.stdin.read().split()
    q = int(tok[0]); p = 1
    out = []
    while q:
        q -= 1
        n = int(tok[p]); p += 1
        arr = list(map(int, tok[p:p + n])); p += n
        if n > 4:
            out.append("NO")
            continue
        order = sorted(range(n), key=lambda k: -arr[k])
        s = [arr[k] for k in order]
        big = s[0]
        uv = [(0, 0)]
        if n > 1: uv.append((big + s[1], big - s[1]))
        if n > 2: uv.append((big - s[2], big + s[2]))
        if n > 3: uv.append((big + s[3], big + s[3]))
        res = [None] * n
        for t, k in enumerate(order):
            u, v = uv[t]
            res[k] = "%d %d" % ((u + v) // 2, (u - v) // 2)
        out.append("YES")
        out.extend(res)
    sys.stdout.write("\n".join(out) + "\n")
main()
