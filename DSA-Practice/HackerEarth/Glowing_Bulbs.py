"""
Problem   : Glowing Bulbs
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/glowing-bulbs/
Difficulty: Hard
Topics    : Algorithms, Binary Search, Searching
Date      : 2026-10-13

Approach:
    Find the k-th positive integer divisible by at least one "active" prime
    (those p where s[p-1] == '1').
    1. Count how many integers in [1, n] are divisible by at least one active
       prime using inclusion-exclusion over all non-empty subsets of active
       primes (sign = (-1)^(|subset|+1), term = n // product).
    2. Subset products are built incrementally from the lowest set bit, and
       products larger than the upper bound are dropped. The rest are sorted
       so count() can stop early once p > n.
    3. Binary search on n in [1, k * smallest_active_prime], since that
       is a guaranteed upper bound for the k-th valid number. The answer
       is the smallest n with count(n) >= k.

Complexity (per test case, m = number of active primes <= 12):
    Time  : O(2^m * (m + log(k * p_min)))
            2^m subset build + sort, then 2^m work per binary-search step
    Space : O(2^m) for the subset products, signs and terms
"""


# -------------------------------------------- Solution ------------------------------------------------------------


import sys

def solve():
    data = iter(sys.stdin.buffer.read().split())
    t = int(next(data))
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    out = []
    for _ in range(t):
        s = next(data).decode()
        k = int(next(data))
        active = [p for p in primes if s[p - 1] == '1']
        m = len(active)
        high = k * active[0]
        low = 1
        size = 1 << m
        products = [1] * size
        signs = [0] * size
        terms = []
        for mask in range(1, size):
            bit = mask & -mask
            i = bit.bit_length() - 1
            prev = mask ^ bit
            products[mask] = products[prev] * active[i]
            signs[mask] = -signs[prev] if prev else 1
            p = products[mask]
            if p <= high:
                terms.append((p, signs[mask]))
        terms.sort()
        def count(n):
            total = 0
            for p, sign in terms:
                if p > n:
                    break
                total += sign * (n // p)
            return total
        while low < high:
            mid = (low + high) // 2
            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1
        out.append(str(low))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()
