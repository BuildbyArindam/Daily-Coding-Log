"""
Problem   : Mex Sort (MEXSUBSORT)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MEXSUBSORT
Date      : 2026-10-07
Difficulty: Hard
Topics    : Constructive, Permutations, MEX

Approach:
  - Record where[v], the position of each value v. If the permutation is
    already sorted, the answer is 0 operations.
  - Scan mex = 1..n-1 while tracking the span [left, right] of positions
    holding 0..mex-1. A value whose position lies strictly inside that span
    is "enclosed" by the smaller values.
      * If an enclosed value already sits at its own index, one operation
        on all other indices finishes the job.
      * Otherwise remember the first enclosed value as the one to fix.
      * If no value is enclosed, no answer exists, so print -1.
  - Otherwise build an intermediate array b in two steps. Op 1 moves a -> b
    and leaves the enclosed position untouched. Op 2 moves b -> identity and
    leaves a chosen pivot untouched. The pivot and the two end slots are
    picked so the reserved values (m, pivot, 0, 1) stay distinct. If no valid
    pivot exists (n too small), print -1.

Complexity: O(n) time per test case (O(n) for the list removal and the
            construction), O(n) space. Output is O(n) per operation, at
            most 2 operations.
"""


# ------------------------------------------ Solution -----------------------------------------------


import sys

def build_answer(a):
    n = len(a)
    where = [0] * n
    already = True
    for idx, val in enumerate(a):
        where[val] = idx
        if idx != val:
            already = False
    if already:
        return []
    left_edge = right_edge = where[0]
    first_mex = -1
    one_step = -1
    for mex in range(1, n):
        p = where[mex]
        if left_edge < p < right_edge:
            if p == mex:
                one_step = mex
                break
            if first_mex == -1:
                first_mex = mex
        if p < left_edge:
            left_edge = p
        elif p > right_edge:
            right_edge = p
    if one_step != -1:
        frozen = one_step
        ids = list(range(n))
        ids.remove(frozen)
        vals = ids[:]
        return [(ids, vals)]
    if first_mex == -1:
        return None
    m = first_mex
    frozen_pos = where[m]
    pivot = -1
    left_slot = right_slot = -1
    for k in range(2, n - 1):
        if k == m or k == frozen_pos:
            continue
        lo = 0
        if lo == frozen_pos:
            lo = 1
        hi = n - 1
        while hi == frozen_pos or hi == k:
            hi -= 1
        if lo < k < hi:
            pivot = k
            left_slot = lo
            right_slot = hi
            break
    if pivot == -1:
        return None
    b = a[:]
    b[frozen_pos] = m
    b[pivot] = pivot
    b[left_slot] = 0
    b[right_slot] = 1
    reserved_positions = {
        frozen_pos,
        pivot,
        left_slot,
        right_slot,
    }
    forbidden_values = {m, pivot, 0, 1}
    rest_values = [
        x for x in range(n)
        if x not in forbidden_values
    ]
    rest_positions = [
        i for i in range(n)
        if i not in reserved_positions
    ]
    for idx, val in zip(rest_positions, rest_values):
        b[idx] = val
    op1_idx = [i for i in range(n) if i != frozen_pos]
    op1_val = [b[i] for i in op1_idx]
    op2_idx = [i for i in range(n) if i != pivot]
    op2_val = op2_idx[:]
    return [
        (op1_idx, op1_val),
        (op2_idx, op2_val),
    ]

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    t = next(it)
    out = []
    for _ in range(t):
        n = next(it)
        p = [next(it) for _ in range(n)]
        ans = build_answer(p)
        if ans is None:
            out.append("-1")
            continue
        out.append(str(len(ans)))
        for indices, values in ans:
            out.append(str(len(indices)))
            out.append(" ".join(map(str, indices)))
            out.append(" ".join(map(str, values)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
