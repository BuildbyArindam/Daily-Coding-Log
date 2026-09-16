"""
Problem   : Jumping Over
Platform  : CodeChef (START256D)
Link      : https://www.codechef.com/START256D/problems/JUMPINGOV
Date      : 2026-09-16
Difficulty: Hard 
Topics    : Fenwick Tree (BIT), Inversion Counting, Permutations, Prefix Sums, Greedy

Approach:
  - Build pos[] mapping each value to its index in the permutation.
  - Two Fenwick tree (BIT) sweeps (left-to-right and right-to-left) compute
    left_ok[x] / right_ok[x]: counts of correctly-ordered pairs among values
    1..x and x..n respectively.
  - Base cost = total inversions of the permutation (total_pairs - left_ok[n]).
  - Scan for breakpoints where pos[x] >= pos[x+1] and greedily choose the
    split point minimizing "extra" cost (left_ok[start-1] + right_ok[x+1]).
  - Answer = inversions + 2 * best_extra.

Complexity:
  Time : O(n log n) per test case (two BIT sweeps + linear breakpoint scan)
  Space: O(n) per test case (BIT array + pos/left_ok/right_ok arrays)
"""


# ----------------------------- Solution --------------------------------------


import sys

class BIT:
    def __init__(self, size):
        self.n = size
        self.t = [0] * (size + 1)
    def add(self, x, val=1):
        x += 1
        while x <= self.n:
            self.t[x] += val
            x += x & -x
    def pref(self, x):
        s = 0
        while x > 0:
            s += self.t[x]
            x -= x & -x
        return s

def solve_case(p):
    n = len(p)
    pos = [0] * (n + 1)
    for i, x in enumerate(p):
        pos[x] = i
    left_ok = [0] * (n + 1)
    fw = BIT(n)
    for x in range(1, n + 1):
        left_ok[x] = left_ok[x - 1] + fw.pref(pos[x])
        fw.add(pos[x])
    right_ok = [0] * (n + 2)
    fw = BIT(n)
    inserted = 0
    for x in range(n, 0, -1):
        not_after = fw.pref(pos[x] + 1)
        after = inserted - not_after
        right_ok[x] = right_ok[x + 1] + after
        fw.add(pos[x])
        inserted += 1
    total_pairs = n * (n - 1) // 2
    inversions = total_pairs - left_ok[n]
    best_extra = 10**30
    start = 1
    for x in range(1, n):
        if pos[x] >= pos[x + 1]:
            extra = left_ok[start - 1] + right_ok[x + 1]
            if extra < best_extra:
                best_extra = extra
            start = x + 1
    extra = left_ok[start - 1] + right_ok[n + 1]
    if extra < best_extra:
        best_extra = extra
    return inversions + 2 * best_extra

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    t = next(it)
    out = []
    for _ in range(t):
        n = next(it)
        perm = [next(it) for _ in range(n)]
        out.append(str(solve_case(perm)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
