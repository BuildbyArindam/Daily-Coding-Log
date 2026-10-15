"""
Problem   : Magical Candy Store (CNDYGAME)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CNDYGAME
Difficulty: 2001
Topics    : Game Theory, Prefix Sum
Date      : 2026-10-15

Approach
--------
The game runs over a circular array of piles, and each query R asks for the
total after R turns. The solution splits R into two parts:
  1. Bulk part (R - 8 turns): the optimal move at each position follows a fixed
     pattern, so it is precomputed once per test. Prefix sums are kept for both
     parity states (s0, s1), and a prefix XOR (xr) records whether the roles
     flip at each position. Full laps of the array are then answered in O(1)
     from the per-lap totals g0, g1, which alternate when the roles flip an
     odd number of times per lap.
  2. Tail part (last <= 8 turns): the best move depends on what follows, so it
     is solved exactly by a backward DP over (mine, opponent's) values,
     maximizing my total and breaking ties by minimizing the opponent's.
     Results are memoized on (last position, tail length).

Complexity
----------
Time : O(N) preprocessing per test, then O(1) per query plus an O(8) tail
       computation the first time each (last, k) pair is seen.
Space: O(N) for the prefix arrays, plus the memo (at most N * 8 entries).
"""


# ------------------------------------------------ Solution -----------------------------------------------------------


import sys

MOD = 10**9 + 7
TAILLEN = 8
_memo = {}

def answer_queries(data, ptr, out):
    n = int(data[ptr]); ptr += 1
    arr = [int(v) for v in data[ptr:ptr + n]]; ptr += n
    q = int(data[ptr]); ptr += 1
    _memo.clear()
    s0, s1, xr = prepare(arr)
    g0, g1, tog = s0[n], s1[n], xr[n + 1]
    for _ in range(q):
        R = int(data[ptr]); ptr += 1
        k = R if R < TAILLEN else TAILLEN
        pre = R - k
        last = (R - 1) % n + 1
        key = (last, k)
        if key not in _memo:
            _memo[key] = tail_exact(arr, n, last, k)
        hh, oo = _memo[key]
        full, rem = divmod(pre, n)
        if tog:
            total = ((full + 1) // 2) * g0 + (full // 2) * g1
        else:
            total = full * g0
        u = (full * tog) & 1
        total += s1[rem] if u else s0[rem]
        total += hh if xr[rem + 1] == u else oo
        out.append(total % MOD)
    return ptr

def tail_exact(arr, n, last, k):
    H = arr[last - 1]
    O = 0
    for i in range(k - 1):
        j = (last - 2 - i) % n + 1
        a = arr[j - 1]
        odd = a & 1
        endpos = (j == n)
        best = None
        if endpos:
            c_me, c_op = 1 - odd, odd
            can_me, can_op = True, a != 1
        else:
            c_me, c_op = odd, 1 - odd
            can_me, can_op = a != 1, True
        if can_me:
            best = (a - c_me + H, O)
        if can_op:
            cand = (a - c_op + O, H)
            if best is None or cand[0] > best[0] or (cand[0] == best[0] and cand[1] < best[1]):
                best = cand
        H, O = best
    return H, O

def prepare(arr):
    n = len(arr)
    s0 = [0] * (n + 1)
    s1 = [0] * (n + 1)
    xr = [0] * (n + 2)
    cur = 0
    t0 = t1 = 0
    for j in range(1, n + 1):
        a = arr[j - 1]
        endpos = (j == n)
        if a == 1:
            opp = not endpos
        else:
            nj = 1 if endpos else j + 1
            opp = (arr[nj - 1] == 1 and nj != n)
        odd = a & 1
        if endpos:
            cost = odd if opp else 1 - odd
        else:
            cost = (1 - odd) if opp else odd
        xr[j] = cur
        if cur:
            t1 += a - cost
        else:
            t0 += a - cost
        s0[j] = t0
        s1[j] = t1
        if opp:
            cur ^= 1
    xr[n + 1] = cur
    return s0, s1, xr

def main():
    data = sys.stdin.buffer.read().split()
    ptr = 1
    out = []
    for _ in range(int(data[0])):
        ptr = answer_queries(data, ptr, out)
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
