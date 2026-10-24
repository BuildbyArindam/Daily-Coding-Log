"""
Problem : Lucky Number (LUCKY2)
Platform: CodeChef
Link    : https://www.codechef.com/problems/LUCKY2
Rating  : 2015
Topics  : Digit DP, Combinatorics, Modular Arithmetic
Date    : 2026-10-24

Approach
--------
Count integers in [L, R] whose number of lucky digits (4 or 7) is itself a
lucky number (a number made only of 4s and 7s).
- The digit count of any input is at most ~1000, so only lucky numbers
  <= 1005 can be targets. Precompute them (14 values).
- Digit DP: f(S) = count of x in [0, S) that are good. Walk the digits of S;
  at each position try every smaller digit c, then fill the `rest` free
  positions. Each free position has 2 lucky choices and 8 non-lucky choices,
  so the number of fillings with exactly j lucky digits is
  C(rest, j) * 2^j * 8^(rest - j).
- Sum that over all targets t, with j = t - (lucky digits already fixed).
- Answer = f(R) + good(R) - f(L), mod 1e9+7.
- Precompute factorials, inverse factorials, and powers of 2 and 8 up to 1005.

Complexity
----------
Precompute: O(LIM)
Per query : O(n * 10 * |T|), n = number of digits (~1000), |T| = 14
Space     : O(LIM + |T|)
"""


# ------------------------------------------------- Solution ---------------------------------------------------------


import sys

MD = 10**9 + 7
LIM = 1005

def solve_all():
    tok = sys.stdin.read().split()
    q = int(tok[0])
    targets = set()
    stack = [4, 7]
    while stack:
        v = stack.pop()
        if v > LIM:
            continue
        targets.add(v)
        stack.append(v * 10 + 4)
        stack.append(v * 10 + 7)

    fa = [1] * (LIM + 1)
    for i in range(1, LIM + 1):
        fa[i] = fa[i - 1] * i % MD
    iv = [1] * (LIM + 1)
    iv[LIM] = pow(fa[LIM], MD - 2, MD)
    for i in range(LIM, 0, -1):
        iv[i - 1] = iv[i] * i % MD
    p2 = [1] * (LIM + 1)
    p8 = [1] * (LIM + 1)
    for i in range(1, LIM + 1):
        p2[i] = p2[i - 1] * 2 % MD
        p8[i] = p8[i - 1] * 8 % MD

    def ways(m, j):
        if j < 0 or j > m:
            return 0
        return fa[m] * iv[j] % MD * iv[m - j] % MD * p2[j] % MD * p8[m - j] % MD

    def below(s):
        n = len(s)
        have = 0
        acc = 0
        for pos in range(n):
            dg = ord(s[pos]) - 48
            rest = n - pos - 1
            for c in range(dg):
                base = have + (1 if c == 4 or c == 7 else 0)
                for t in targets:
                    acc += ways(rest, t - base)
            acc %= MD
            if dg == 4 or dg == 7:
                have += 1
        return acc

    def is_good(s):
        cnt = s.count('4') + s.count('7')
        return 1 if cnt in targets else 0

    out = []
    for z in range(q):
        lo = tok[1 + 2 * z]
        hi = tok[2 + 2 * z]
        res = (below(hi) + is_good(hi) - below(lo)) % MD
        out.append(str(res))
    print("\n".join(out))

solve_all()
