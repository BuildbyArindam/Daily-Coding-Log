"""
Problem   : Progressive Purge (APDIS)
Link      : https://www.codechef.com/problems/APDIS
Date      : 2026-08-28
Platform  : CodeChef (Starters 253)
Difficulty: Easy (official) — treated as Medium-Hard for this optimized approach
Topics    : Dynamic Programming, Divisors/Number Theory, Binary Search, Offline Queries

Approach:
  A subarray is "good" if it can be sorted by deleting indices forming an
  arithmetic progression (common difference d >= 2). For each left endpoint L,
  we need the farthest right endpoint R such that A[L..R] is good.

  Instead of the standard O(N^2) editorial approach (loop over every d from 2..N
  and run an O(N) DP per d), this solution precomputes, for each L, the single
  descent index and the "one-deletion" reach directly, then batches the harder
  "two-deletion, fixed spacing d" cases per divisor d. For each d, valid queries
  are grouped by residue class mod d, and the farthest safe extension is found
  via binary search over sorted descent/bad-middle positions per residue class,
  using precomputed divisor lists (sieve up to MAXN) to only test relevant d's.

Time complexity : O(N^2 / d-ish amortized) dominated by divisor enumeration
                   (~O(N log N) divisor pairs) times O(log N) binary search
                   per candidate => roughly O(N log^2 N) in practice, well
                   under the O(N^2) editorial bound for N <= 4000.
Space complexity : O(N log N) for the divisor table + O(N) auxiliary arrays.
"""


# ----------------------------- Solution ------------------------------------


import sys
from bisect import bisect_left, bisect_right

MAXN = 4000
divisors = [[] for _ in range(MAXN + 1)]
for d in range(2, MAXN + 1):
    for v in range(d, MAXN + 1, d):
        divisors[v].append(d)

def solve_case(a):
    n = len(a)
    if n == 1:
        return 1
    desc = [i for i in range(n - 1) if a[i] > a[i + 1]]
    k = len(desc)
    if k == 0:
        return n * (n + 1) // 2
    rank = [-1] * n
    for i, p in enumerate(desc):
        rank[p] = i
    next_desc = [n - 1] * n
    cur = n - 1
    for i in range(n - 2, -1, -1):
        if a[i] > a[i + 1]:
            cur = i
        next_desc[i] = cur
    nondec_end = [0] * n
    nondec_end[n - 1] = n - 1
    for i in range(n - 2, -1, -1):
        if a[i] <= a[i + 1]:
            nondec_end[i] = nondec_end[i + 1]
        else:
            nondec_end[i] = i
    bad_middle = [
        i for i in range(1, n - 1)
        if a[i - 1] > a[i + 1]
    ]
    one_end = [0] * n
    queries = [None] * (n + 1)
    answer = 0
    for L in range(n):
        p = next_desc[L]
        if p == n - 1:
            one_end[L] = n - 1
            answer += n - L
            continue
        best_one = p
        if p == L or a[p - 1] <= a[p + 1]:
            best_one = max(best_one, nondec_end[p + 1])
        x = p + 1
        if x == n - 1:
            best_one = max(best_one, x)
        elif a[p] <= a[p + 2]:
            best_one = max(best_one, nondec_end[p + 2])
        else:
            best_one = max(best_one, x)
        one_end[L] = best_one
        answer += best_one - L + 1
        if best_one == n - 1:
            continue
        q = next_desc[p + 1]
        if q == n - 1:
            continue
        lower = max(best_one + 1, q + 1)
        if lower >= n:
            continue
        candidates = set()
        for x in (p, p + 1):
            for y in (q, q + 1):
                diff = y - x
                if diff >= 2:
                    for d in divisors[diff]:
                        candidates.add((d, x))
        for d, x in candidates:
            if queries[d] is None:
                queries[d] = []
            queries[d].append((L, x))
    best_multi = [-1] * n
    for d in range(2, n + 1):
        qs = queries[d]
        if not qs:
            continue
        descent_groups = [[] for _ in range(d)]
        for p in desc:
            descent_groups[p % d].append(p)
        middle_groups = [[] for _ in range(d)]
        for p in bad_middle:
            middle_groups[p % d].append(p)
        for L, x in qs:
            p = next_desc[L]
            q = next_desc[p + 1]
            q_rank = rank[q]
            r = x % d
            r_prev = (r - 1) % d
            g0 = descent_groups[r]
            g1 = descent_groups[r_prev]
            first_bad_descent = n - 1
            start = q_rank + 1
            if start < k:
                base0 = bisect_right(g0, q)
                base1 = bisect_right(g1, q)
                lo = start
                hi = k - 1
                while lo < hi:
                    mid = (lo + hi) // 2
                    pos = desc[mid]
                    allowed = (
                        bisect_right(g0, pos) - base0
                        + bisect_right(g1, pos) - base1
                    )
                    total = mid - q_rank
                    if total > allowed:
                        hi = mid
                    else:
                        lo = mid + 1
                pos = desc[lo]
                if pos % d not in (r, r_prev):
                    first_bad_descent = pos
            mg = middle_groups[r]
            idx = bisect_left(mg, L + 1)
            if idx < len(mg):
                first_bad_middle = mg[idx]
            else:
                first_bad_middle = n - 1
            cap = min(first_bad_descent, first_bad_middle)
            if cap > best_multi[L]:
                best_multi[L] = cap
    for L in range(n):
        if one_end[L] == n - 1:
            continue
        p = next_desc[L]
        q = next_desc[p + 1]
        if q == n - 1:
            continue
        lower = max(one_end[L] + 1, q + 1)
        if lower < n and best_multi[L] >= lower:
            answer += best_multi[L] - lower + 1
    return answer

def main():
    input = sys.stdin.buffer.readline
    T = int(input())
    out = []
    for _ in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        while len(a) < n:
            a.extend(map(int, input().split()))
        out.append(str(solve_case(a)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
