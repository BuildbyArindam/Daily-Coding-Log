"""
Problem   : Chef and Magical Steps (CHEFMGX), CodeChef
Link      : https://www.codechef.com/problems/CHEFMGX
Date      : 2026-10-16
Difficulty: 2004
Topics    : Number Theory, Sieve of Eratosthenes, Prefix Sums

Approach  : Read all queries at once and sieve primes up to the largest
            upper bound. A prefix-sum array of prime counts then gives the
            number of primes in any range in O(1). Each answer is
            (hi - lo) minus the primes in [lo + 2, hi]. The query step is
            fully vectorized with NumPy.

Time      : O(M log log M + Q), where M = max(hi) and Q = number of queries
Space     : O(M + Q)
"""


# -------------------------------------------------- Solution ---------------------------------------------------------------


import sys
import numpy as np

def build_prime_prefix(limit):
    flags = np.ones(limit + 1, dtype=np.bool_)
    flags[:2] = False
    r = int(limit ** 0.5) + 1
    for d in range(2, r + 1):
        if flags[d]:
            flags[d * d::d] = False
    return np.cumsum(flags, dtype=np.int32)

def main():
    raw = sys.stdin.buffer.read().split()
    q = int(raw[0])
    nums = np.array(raw[1:1 + 2 * q], dtype=np.int64)
    hi = nums[1::2]
    lo = nums[0::2]
    prefix = build_prime_prefix(int(hi.max()) + 2)
    primes_inside = prefix[hi] - prefix[lo + 1]
    result = (hi - lo) - primes_inside
    sys.stdout.write("\n".join(map(str, result.tolist())) + "\n")

main()
