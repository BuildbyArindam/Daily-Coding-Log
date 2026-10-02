"""
Platform   : HackerEarth
Problem    : Base numbers
Link       : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/in-another-base-1-e0d0f1ca/
Difficulty : Easy
Topics     : Algorithms, Binary Search, Searching
Date       : 2026-10-02

Approach:
    Count x in [1, 10^9] such that a * x^x has exactly n digits in base b,
    i.e. b^(n-1) <= a * x^x < b^n.
    Since a * x^x is monotonically increasing in x, the answer is
    first_ge(n) - first_ge(n-1), where first_ge(k) is the smallest x with
    a * x^x >= b^k.
    - Binary search on x using logarithms: log(a) + x*log(x) >= k*log(b),
      which avoids huge-integer arithmetic.
    - Floating-point error is fixed by stepping a few positions around the
      result and comparing precisely: an exact prime-exponent check for
      equality, then high-precision Decimal logs for near-ties.

Time  : O(Q * log(LIMIT)) for the binary search, plus O(1) boundary
        corrections per query (LIMIT = 10^9, so about 30 iterations).
Space : O(1) extra per query (O(Q) for buffered output).
"""


# ------------------------------------- Solution ------------------------------------------------------


import sys
import math
from decimal import Decimal, getcontext
getcontext().prec = 80
LIMIT = 10**9
PRIMES = (2, 3, 5, 7)

def exact_equal(a, x, b, k):
    if k < 0:
        return False
    aa = a
    xx = x
    bb = b
    for p in PRIMES:
        ca = 0
        cx = 0
        cb = 0
        while aa % p == 0:
            aa //= p
            ca += 1
        while xx % p == 0:
            xx //= p
            cx += 1
        while bb % p == 0:
            bb //= p
            cb += 1
        if ca + x * cx != k * cb:
            return False
    return aa == 1 and xx == 1 and bb == 1

def compare(a, x, b, k, log_a, log_b):
    if k == 0:
        return 1
    value = log_a + x * math.log(x) - k * log_b
    if value > 1e-4:
        return 1
    if value < -1e-4:
        return -1
    if exact_equal(a, x, b, k):
        return 0
    dx = Decimal(x)
    lhs = Decimal(a).ln() + dx * dx.ln()
    rhs = Decimal(k) * Decimal(b).ln()
    if lhs < rhs:
        return -1
    if lhs > rhs:
        return 1
    return 0

def first_ge(a, k, b):
    if k <= 0:
        return 1
    log_a = math.log(a)
    log_b = math.log(b)
    lo, hi = 1, LIMIT
    while lo < hi:
        mid = (lo + hi) // 2
        value = log_a + mid * math.log(mid) - k * log_b
        if value >= 0:
            hi = mid
        else:
            lo = mid + 1
    x = max(1, lo - 3)
    while x > 1 and compare(a, x - 1, b, k, log_a, log_b) >= 0:
        x -= 1
    while x <= LIMIT and compare(a, x, b, k, log_a, log_b) < 0:
        x += 1
    return x

def solve():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        a, n, b = map(int, line.split())
        left = first_ge(a, n - 1, b)
        right = first_ge(a, n, b)
        right = min(right, LIMIT + 1)
        out.append(str(max(0, right - left)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
