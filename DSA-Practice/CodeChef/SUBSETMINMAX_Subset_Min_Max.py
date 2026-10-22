"""
Problem   : Subset Min Max (SUBSETMINMAX)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SUBSETMINMAX
Difficulty: 1983
Topics    : Sorting, Convex Hull Trick
Date      : 2026-10-22

Approach:
  Sort the elements by value, then sweep left to right. Each element is
  treated as the larger endpoint, and the best smaller partner is found by
  maximizing a linear function of the current value. Earlier elements become
  lines (slope = value, intercept = x * (b - ones_before)) in an upper convex
  hull (Convex Hull Trick). Since slopes are added in sorted order and queries
  also come in increasing value, the optimal line only moves forward, so a
  monotone pointer answers each query in amortized O(1). Single-element
  subsets are handled separately.

Complexity:
  Time : O(n log n) per test case (sorting dominates; hull build and
         queries are amortized O(n))
  Space: O(n)
"""


# ------------------------------------------ Solution ------------------------------------------------------


import sys

def solve_case(n, x, vals, bits):
    pairs = sorted(zip(vals, bits))
    k = 0
    for _, b in pairs:
        k += b
    ans = -x * k   
    base = -x * k - 2 * x
    ones_before = 0
    ms = []  
    cs = []  
    ptr = 0
    for v, b in pairs:
        single = v * v - x * (k + 1 - 2 * b)
        if single > ans:
            ans = single
        if ms:
            if ptr >= len(ms):
                ptr = len(ms) - 1
            while ptr + 1 < len(ms) and ms[ptr + 1] * v + cs[ptr + 1] >= ms[ptr] * v + cs[ptr]:
                ptr += 1
            cand = ms[ptr] * v + cs[ptr] + x * (ones_before + 2 * b) + base
            if cand > ans:
                ans = cand
        c = x * (b - ones_before)
        skip = False
        if ms and ms[-1] == v:
            if cs[-1] >= c:
                skip = True
            else:
                ms.pop()
                cs.pop()
        if not skip:
            while len(ms) >= 2:
                m1, c1 = ms[-2], cs[-2]
                m2, c2 = ms[-1], cs[-1]
                if (c - c1) * (m2 - m1) >= (c2 - c1) * (v - m1):
                    ms.pop()
                    cs.pop()
                else:
                    break
            ms.append(v)
            cs.append(c)
        ones_before += b
    return ans

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    res = []
    while t:
        t -= 1
        n = int(data[pos]); x = int(data[pos + 1]); pos += 2
        vals = list(map(int, data[pos:pos + n])); pos += n
        raw = data[pos]; pos += 1
        bits = [ch - 48 for ch in raw]
        res.append(solve_case(n, x, vals, bits))
    sys.stdout.write("\n".join(map(str, res)) + "\n")

main()
