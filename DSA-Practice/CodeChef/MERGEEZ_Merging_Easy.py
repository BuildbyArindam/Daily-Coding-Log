"""
Platform   : CodeChef
Problem    : Merging (Easy) - MERGEEZ
Link       : https://www.codechef.com/problems/MERGEEZ
Date       : 2026-10-14
Difficulty : Hard
Topics     : Dynamic Programming, Prefix Sums, Monotonic Stack, Counting (mod 998244353)

Approach:
  - A monotonic stack gives pg[i], the nearest index to the left with a larger
    value than p[i]. It bounds the range of valid transitions for each prefix.
  - A DP over prefix length r keeps two count arrays (pre_a, pre_b), each indexed
    by [prefix position][state]. The row range [lo, r] is read as a difference of
    prefix sums, so each transition is O(1) per state instead of a nested loop.
  - The two states swap roles on each transition, which is why fa and fb are
    reversed copies of each other. At r = n the two states are combined into
    the final answer vector.
  - Each DP row is computed with NumPy vector operations, with all values
    kept mod 998244353.

Complexity:
  Time  : O(N^2) per test case (N rows x O(N) vectorised work per row)
  Space : O(N^2) for the two prefix tables (pre_a, pre_b)
"""


# ----------------------------------------------- Solution ---------------------------------------------------


import sys
import numpy as np

MOD = 998244353

def prev_greater(p, n):
    res = [0] * (n + 2)
    stack = []
    for q in range(1, n + 1):
        while stack and p[stack[-1]] < p[q]:
            stack.pop()
        res[q] = stack[-1] if stack else 0
        stack.append(q)
    return res

def solve_case(n, p):
    pg = prev_greater(p, n)
    width = n + 1
    pre_a = np.zeros((n + 2, width), dtype=np.int64) 
    pre_b = np.zeros((n + 2, width), dtype=np.int64) 
    pre_a[1, 0] = 1
    pre_b[1, 0] = 1
    answer = None
    for r in range(1, n + 1):
        lo = pg[r + 1] if r < n else 0
        if lo > r - 1:
            fa = np.zeros(r + 1, dtype=np.int64)
            fb = np.zeros(r + 1, dtype=np.int64)
            da = fa
        else:
            db = (pre_b[r, :r + 1] - pre_b[lo, :r + 1]) % MOD
            da = (pre_a[r, :r + 1] - pre_a[lo, :r + 1]) % MOD
            fa = db[::-1]
            fb = da[::-1]
        if r == n:
            tmp = np.zeros(width, dtype=np.int64)
            tmp += fa
            tmp += da
            answer = tmp % MOD
            break
        pre_a[r + 1] = pre_a[r]
        pre_a[r + 1, :r + 1] += fa
        pre_a[r + 1] %= MOD
        pre_b[r + 1] = pre_b[r]
        pre_b[r + 1, :r + 1] += fb
        pre_b[r + 1] %= MOD
    return answer

def main():
    tokens = sys.stdin.buffer.read().split()
    cases = int(tokens[0])
    cursor = 1
    lines = []
    for _ in range(cases):
        n = int(tokens[cursor])
        cursor += 1
        p = [0] + [int(x) for x in tokens[cursor:cursor + n]]
        cursor += n
        res = solve_case(n, p)
        lines.append(" ".join(map(str, res.tolist())))
    sys.stdout.write("\n".join(lines) + "\n")

main()
