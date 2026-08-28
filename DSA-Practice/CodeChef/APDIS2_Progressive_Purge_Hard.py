"""
Problem   : Progressive Purge (Hard)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/APDIS2
Solved on : 2026-08-28

Approach:
  For each subarray [L, R] to be "good", it must be sortable by deleting
  elements at indices forming an AP with common difference d >= 2. Any
  valid d can be reduced to one of its prime factors, so only primes
  need to be checked. For d <= sqrt(N), brute-force a linear DP per d.
  For d > sqrt(N): observe any useful d must divide the gap between two
  consecutive "descents" (a[i] > a[i+1]); since gaps sum to <= N, there
  are only O(sqrt(N)) distinct large-prime candidates worth checking.
  A smallest-prime-factor (SPF) sieve extracts these candidate primes
  from each gap in O(log gap). For each candidate d, a mod-d bucket DP
  (tracking up to 3 "recently updated" residues + a global fallback)
  computes, for every start index i, the farthest reachable sorted
  right endpoint. Answers are summed as ri[i] - i + 1.

Time complexity  : O(N * sqrt(N))  per test case (amortized over candidates)
Space complexity : O(N)            (SPF sieve + per-candidate buckets)
"""


# -------------------------------- Solution ------------------------------


import sys
from math import isqrt

def solve_case(n, vals, lpf):
    if n == 1:
        return 1
    a = [0] + vals + [n + 1, n + 1]
    bad1 = bytearray(n + 2)
    bad2 = bytearray(n + 2)
    has_bad = False
    for i in range(1, n):
        if a[i] > a[i + 1]:
            bad1[i] = 1
            has_bad = True
    if not has_bad:
        return n * (n + 1) // 2
    for i in range(1, n - 1):
        if a[i] > a[i + 2]:
            bad2[i] = 1
    seen = bytearray(n + 1)
    cand = [2]
    seen[2] = 1
    prev1 = -1   
    prev2 = -1   
    def add_prime_factors(x):
        while x >= 2:
            p = lpf[x]
            if not seen[p]:
                seen[p] = 1
                cand.append(p)
            while x % p == 0:
                x //= p
    for i in range(n - 1, 0, -1):
        if bad1[i]:
            v = prev1
            if v == i + 1:
                v = prev2
            if v != -1:
                g = v - i
                if g - 1 >= 2:
                    add_prime_factors(g - 1)
                add_prime_factors(g)
                add_prime_factors(g + 1)
            prev2 = prev1
            prev1 = i
    K = len(cand)
    glob = [n] * K
    c1 = [-1] * K
    c2 = [-1] * K
    c3 = [-1] * K
    v1 = [0] * K
    v2 = [0] * K
    v3 = [0] * K
    cnt = [0] * K
    cur = [n] * K
    freq = [0] * (n + 1)
    freq[n] = K
    global_max = n
    answer = 0
    for i in range(n, 0, -1):
        b1 = bad1[i]
        b2 = bad2[i]
        if b1 or b2:
            for k in range(K):
                d = cand[k]
                x1 = i % d
                x2 = x1 + 1
                if x2 == d:
                    x2 = 0
                if b1:
                    old_c1 = c1[k]
                    old_c2 = c2[k]
                    old_c3 = c3[k]
                    old_glob = glob[k]
                    if x1 == old_c1:
                        nv1 = v1[k]
                    elif x1 == old_c2:
                        nv1 = v2[k]
                    elif x1 == old_c3:
                        nv1 = v3[k]
                    else:
                        nv1 = old_glob
                    if x2 == old_c1:
                        nv2 = v1[k]
                    elif x2 == old_c2:
                        nv2 = v2[k]
                    elif x2 == old_c3:
                        nv2 = v3[k]
                    else:
                        nv2 = old_glob
                    glob[k] = i
                    c1[k] = x1
                    v1[k] = nv1
                    c2[k] = x2
                    v2[k] = nv2
                    c3[k] = -1
                    cnt[k] = 2
                if b2:
                    nv = i + 1
                    if x2 == c1[k]:
                        v1[k] = nv
                    elif x2 == c2[k]:
                        v2[k] = nv
                    elif x2 == c3[k]:
                        v3[k] = nv
                    else:
                        c3[k] = x2
                        v3[k] = nv
                        cnt[k] += 1
                mx = glob[k]
                z = v1[k]
                if z > mx:
                    mx = z
                z = v2[k]
                if z > mx:
                    mx = z
                if c3[k] != -1:
                    z = v3[k]
                    if z > mx:
                        mx = z
                if cnt[k] == d:
                    mx = v1[k]
                    if v2[k] > mx:
                        mx = v2[k]
                    if c3[k] != -1 and v3[k] > mx:
                        mx = v3[k]
                old = cur[k]
                if mx != old:
                    freq[old] -= 1
                    freq[mx] += 1
                    cur[k] = mx
                    if mx > global_max:
                        global_max = mx
        while global_max > 1 and freq[global_max] == 0:
            global_max -= 1
        answer += global_max - i + 1
    return answer

def build_lpf(max_n):
    """
    lpf[x] = largest prime factor of x.
    """
    lpf = [0] * (max_n + 1)
    for p in range(2, max_n + 1):
        if lpf[p] == 0:  # p is prime
            for x in range(p, max_n + 1, p):
                lpf[x] = p
    return lpf

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    T = next(it)
    tests = []
    max_n = 1
    for _ in range(T):
        n = next(it)
        a = [next(it) for _ in range(n)]
        tests.append((n, a))
        if n > max_n:
            max_n = n
    lpf = build_lpf(max_n)
    out = []
    for n, a in tests:
        out.append(str(solve_case(n, a, lpf)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
