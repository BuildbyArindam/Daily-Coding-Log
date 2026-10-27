"""
Problem   : Prime Factor Division (PRIMEFACDIV)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/PRIMEFACDIV
Difficulty: 2016
Topics    : GCD, Prime Divisors, Number Theory, Integer Factorisation, Divisors
Date      : 2026-10-27

Approach:
    For each pair (p, q), strip from q every prime factor it shares with p.
    Repeatedly divide q by gcd(p, q) until the gcd becomes 1. What remains
    holds only primes that do not divide p. If the remainder is 1, every
    prime factor of q also divides p -> "YES", otherwise "NO".
    This avoids factorising anything explicitly.

Complexity:
    Time : O(T * log^2(max(q)))  -- each loop pass at least halves q (O(log q) passes),
                                    and each pass costs one gcd (O(log q))
    Space: O(T) for buffered input/output, O(1) extra per test case
"""


# ------------------------------------------------- Solution ------------------------------------------------------


import sys
from math import gcd as _g

def _reduce(x, y):
    d = _g(x, y)
    while d > 1:
        y //= d
        d = _g(x, y)
    return y

def _run():
    stream = sys.stdin.buffer.read().split()
    total = int(stream[0])
    answers = [None] * total
    idx = 1
    for k in range(total):
        p = int(stream[idx])
        q = int(stream[idx + 1])
        idx += 2
        answers[k] = "NO" if _reduce(p, q) != 1 else "YES"
    sys.stdout.write("\n".join(answers) + "\n")

if __name__ == "__main__":
    _run()
