# =============================================================================
# Platform   : CodeChef
# Problem    : Subtasks (GCDCNT)
# Link       : https://www.codechef.com/problems/GCDCNT
# Difficulty : 2002
# Topics     : Segment Trees, Square Root Decomposition, Divisors, Inclusion Exclusion, Principle, Mobius Inversion, Advanced Data Structures, Advanced Tree Structures, Advanced Algorithms, Mathematics, Number Theory, Set Theory, Integer Factorisation
# Solved on  : 2026-10-16
#
# Approach   : Point updates + range queries for "count of i in [l, r] with
#              gcd(a[i], g) == 1".
#              By Mobius inversion / inclusion-exclusion:
#                  count = sum over squarefree d | g of mu(d) * (#a[i] in [l, r] divisible by d)
#              Solved offline:
#                1. Read all ops; for every divisor d > 1 (squarefree) record every
#                   index that ever holds a multiple of d (initial array + updates).
#                2. Per d, keep a sorted position list and a Fenwick tree over it
#                   (built in O(m) from initial counts).
#                3. Update: remove old value's divisors, add new value's divisors.
#                4. Query: iterate squarefree divisors of g, take the BIT range count
#                   via bisect on the position list, and apply the mu(d) sign.
#              A smallest-prime-factor sieve gives fast factorisation; a number
#              <= 1e5 has at most 6 distinct primes, so <= 64 squarefree divisors.
#
# Time       : O(M log log M) sieve
#              + O((N + Q) * 64 * log(N + Q)) for updates/queries (BIT + bisect)
# Space      : O((N + Q) * 64) for the per-divisor position lists and BITs
# =============================================================================


# --------------------------------------------------- Solution -------------------------------------------------------------


import sys
from bisect import bisect_left, bisect_right

LIM = 100001
smallest = list(range(LIM))

def prep_sieve():
    i = 2
    while i * i < LIM:
        if smallest[i] == i:
            for j in range(i * i, LIM, i):
                if smallest[j] == j:
                    smallest[j] = i
        i += 1

def sqfree(v):
    out = [(1, 1)]
    while v > 1:
        p = smallest[v]
        while v % p == 0:
            v //= p
        out += [(d * p, -s) for d, s in out]
    return out

def fen_add(t, i, delta):
    n = len(t)
    while i < n:
        t[i] += delta
        i += i & -i

def fen_sum(t, i):
    r = 0
    while i > 0:
        r += t[i]
        i -= i & -i
    return r

def answer_all(arr, n, ops):
    where = {}
    for i in range(n):
        for d, _ in sqfree(arr[i]):
            if d > 1:
                where.setdefault(d, []).append(i)
    for op in ops:
        if op[0] == 1:
            x = op[1]
            for d, _ in sqfree(op[2]):
                if d > 1:
                    where.setdefault(d, []).append(x)
    for d in where:
        where[d] = sorted(set(where[d]))
    bit = {d: [0] * (len(p) + 1) for d, p in where.items()}
    for i in range(n):
        for d, _ in sqfree(arr[i]):
            if d > 1:
                bit[d][bisect_left(where[d], i) + 1] += 1
    for d, t in bit.items():
        m = len(t) - 1
        for j in range(1, m + 1):
            k = j + (j & -j)
            if k <= m:
                t[k] += t[j]
    res = []
    for op in ops:
        if op[0] == 1:
            x, y = op[1], op[2]
            if arr[x] == y:
                continue
            for d, _ in sqfree(arr[x]):
                if d > 1:
                    fen_add(bit[d], bisect_left(where[d], x) + 1, -1)
            for d, _ in sqfree(y):
                if d > 1:
                    fen_add(bit[d], bisect_left(where[d], x) + 1, 1)
            arr[x] = y
        else:
            lo, hi, g = op[1], op[2], op[3]
            total = hi - lo + 1
            for d, s in sqfree(g):
                if d == 1 or d not in where:
                    continue
                p = where[d]
                cnt = fen_sum(bit[d], bisect_right(p, hi)) - fen_sum(bit[d], bisect_left(p, lo))
                total += s * cnt
            res.append(total)
    return res

def main():
    tok = sys.stdin.buffer.read().split()
    ptr = 0
    n = int(tok[ptr]); ptr += 1
    arr = [int(x) for x in tok[ptr:ptr + n]]
    ptr += n
    q = int(tok[ptr]); ptr += 1
    ops = []
    for _ in range(q):
        if tok[ptr] == b'1':
            ops.append((1, int(tok[ptr + 1]) - 1, int(tok[ptr + 2])))
            ptr += 3
        else:
            ops.append((2, int(tok[ptr + 1]) - 1, int(tok[ptr + 2]) - 1, int(tok[ptr + 3])))
            ptr += 4
    prep_sieve()
    out = answer_all(arr, n, ops)
    sys.stdout.write("\n".join(map(str, out)) + ("\n" if out else ""))

main()
