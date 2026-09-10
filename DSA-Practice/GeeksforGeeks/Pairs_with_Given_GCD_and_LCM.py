"""
Problem: Pairs with Given GCD and LCM
Link: https://www.geeksforgeeks.org/problems/possible-pairs1550/1
Platform: GeeksforGeeks
Difficulty: Easy
Topic: Mathematics, Factorization
Date: 2026-09-10

Approach:
Given GCD = x and LCM = y, a valid pair (a, b) exists only if y % x == 0.
Let n = y / x. Any such pair must satisfy a = x * m, b = x * k, where
gcd(m, k) = 1 and m * k = n (m, k coprime factors of n).
The number of ways to split n into two coprime factors is 2^d, where d is
the number of DISTINCT prime factors of n (each prime must go entirely to
one side or the other, giving 2 choices per prime).
So: factorize n, count distinct primes, return 2^distinct_primes.

Time Complexity: O(sqrt(n)) for trial division factorization, where n = y/x
Space Complexity: O(1)
"""


# ----------------------------- Solution -----------------------------------------


class Solution:
    def pairCount(self, x, y):
        """code here"""
        if y % x != 0:
            return 0
        n = y // x
        distinct_primes = 0
        p = 2
        while p * p <= n:
            if n % p == 0:
                distinct_primes += 1
                while n % p == 0:
                    n //= p
            p += 1
        if n > 1:
            distinct_primes += 1
        return 1 << distinct_primes
